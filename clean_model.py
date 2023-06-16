import gurobipy as gp
from gurobipy import GRB
from clean_parameters import *

mip = gp.Model('Vertical farm positioning')

USE_SYMMETRY_BREAKING = False
USE_ADVANCED_SYMMETRY_BREAKING = False
# mip.Params.Symmetry = 2

# variables
v = mip.addVars(D, R, F_list, vtype=GRB.BINARY, name='fertillizerTank',)
irr = mip.addVars(D, L, R, P, I_list, vtype=GRB.BINARY, name='irrigationRegime')
cnt = mip.addVars(D, B, L, R, P, vtype=GRB.INTEGER, name='containers', lb=0, ub=c)
h = mip.addVars(D, B, L, R, P, vtype=GRB.BINARY, name='allocated')

# Linearization variables
Dv = mip.addVars(D[1:], R, vtype=GRB.BINARY, name='fertillizerTank')
Dh = mip.addVars(D[1:], B, L, R, P, vtype=GRB.BINARY, name='containers', lb=0, ub=c)

# Simple symmetry breaking variables
if USE_SYMMETRY_BREAKING:   
    y = mip.addVars(D,R, vtype=GRB.BINARY, name='firstDayInUseRack',)

if USE_ADVANCED_SYMMETRY_BREAKING:
    z = mip.addVars(D,R,L, vtype=GRB.BINARY, name='layerInUse')
    u = mip.addVars(D,R,L, vtype=GRB.BINARY, name='layerWillBeTakenInUseToday')

# constraints
mip.addConstrs(gp.quicksum([cnt[(d,b,l,r,p)] for l in L for r in R for p in P]) == nc[(d,b)] for d in D for b in B) # 1
mip.addConstrs(gp.quicksum([cnt[(d,b,l,r,p)] for b in B]) <= c for d in D for l in L for r in R for p in P ) # 2
mip.addConstrs(cnt[(d,b,l,r,p)] <= c * h[(d,b,l,r,p)] for d in D for b in B for l in L for r in R for p in P) # 3
mip.addConstrs(h[(d,b,l,r,p)] <= cnt[(d,b,l,r,p)] for d in D for b in B for l in L for r in R for p in P) # 3

mip.addConstrs(gp.quicksum([ v[(d,r,f)] for f in F_list ]) == 1 for d in D for r in R)
mip.addConstrs(h[(d,b,l,r,p)] <= v[(d,r,F[(d,b)])] for d in D for b in B for l in L for r in R for p in P) # 4

mip.addConstrs(gp.quicksum([ irr[(d,l,r,p,i)] for i in I_list ]) == 1 for d in D for l in L for r in R for p in P)
mip.addConstrs(h[(d,b,l,r,p)] <= irr[(d,l,r,p,I[(d,b)])] for d in D for b in B for l in L for r in R for p in P) # 5

# Linearization constraints
mip.addConstrs(v[(d,r,f)] - v[(d-1,r,f)] <= Dv[(d,r)] for d in D[1:] for r in R for f in F_list) # 1
mip.addConstrs(v[(d-1,r,f)] - v[(d,r,f)] <= Dv[(d,r)] for d in D[1:] for r in R for f in F_list) # 1
mip.addConstrs(h[(d,b,l,r,p)] - h[(d-1,b,l,r,p)] <= Dh[(d,b,l,r,p)] for d in D[1:] for b in B for l in L for r in R for p in P) # 2
mip.addConstrs(h[(d-1,b,l,r,p)] - h[(d,b,l,r,p)] <= Dh[(d,b,l,r,p)] for d in D[1:] for b in B for l in L for r in R for p in P) # 2

# Simple symmetry breaking constraints
if USE_SYMMETRY_BREAKING:
    mip.addConstrs(gp.quicksum([h[(d,b,l,r,p)] for b in B for l in L for p in P]) <= len(B) * len(L) * len(P) * gp.quicksum([y[(i,r)] for i in D[:d]]) for d in D for r in R) # 1
    mip.addConstrs(gp.quicksum([ y[(d,r)] for d in D]) == 1 for r in R) # 2
    mip.addConstrs(y[(d,r)] <= gp.quicksum([ y[i,r-1] for i in D[:d] ]) for d in D for r in R[1:]) # 3

# Advanced symmetry breaking constraints
if USE_ADVANCED_SYMMETRY_BREAKING:
    # Link layer in use to h variables
    mip.addConstrs(h[(d,b,l,r,p)] <= c * z[(d,r,l)] for d in D for r in R for l in L for b in B for p in P)
    mip.addConstrs(z[(d,r,l)] <= h.sum(d,"*",l,r,"*") for d in D for r in R for l in L)

    # Link will be taken in use today to in use variable
    mip.addConstrs(u[(d,r,l)] >= z[(d,r,l)] - z[(d-1,r,l)] for d in D[1:] for r in R for l in L )
    mip.addConstrs(u[(1,r,l)] == z[(1,r,l)] for r in R for l in L)

    # Every time a layer is starting to be used, all layers below it must be in use
    mip.addConstrs(l * u[(d,r,l)] <= gp.quicksum([z[(d,r,i)] for i in L[:l]])  for d in D for r in R for l in L )
    
   
# objective function
Dh_obj = gp.quicksum([Dh[(d,b,l,r,p)] for d in D[1:] for b in B for l in L for r in R for p in P]) 
Dv_obj = gp.quicksum([Dv[(d,r)] for d in D[1:] for r in R])
h_obj = gp.quicksum([h[(d,b,l,r,p)] for d in D for b in B for l in L for r in R for p in P])

mip.setObjectiveN(Dv_obj, 0, 2)
mip.setObjectiveN(Dh_obj, 1,1)
mip.setObjectiveN(h_obj, 2,0)
mip.ModelSense = GRB.MINIMIZE


mip.write('model.lp')
mip.optimize()


for d in D:
    for b in B:
        for l in L:
            for r in R:
                for p in P:
                    if cnt[(d,b,l,r,p)].x > 0:
                        print(F"On D{d} for B{b} at L{l}R{r}P{p} we have {cnt[(d,b,l,r,p)].x}")