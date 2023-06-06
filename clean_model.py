import gurobipy as gp
from gurobipy import GRB
from clean_parameters import *

mip = gp.Model('Vertical farm positioning')

USE_SYMMETRY_BREAKING = True
USE_ADVANCED_SYMMETRY_BREAKING = True
# mip.Params.Symmetry = 2

# variables
v = mip.addVars(D, R, vtype=GRB.INTEGER, name='fertillizerTank', lb=0, ub=max(F_list))
irr = mip.addVars(D, L, R, P, vtype=GRB.INTEGER, name='irrigationRegime', lb=0, ub=max(I_list))
cnt = mip.addVars(D, B, L, R, P, vtype=GRB.INTEGER, name='containers', lb=0)
h = mip.addVars(D, B, L, R, P, vtype=GRB.BINARY, name='allocated')

# Linearization variables
Dv = mip.addVars(D[1:], R, vtype=GRB.BINARY, name='fertillizerTank')
Dcnt = mip.addVars(D[1:], B, L, R, P, vtype=GRB.INTEGER, name='containers', lb=0, ub=c)

# Simple symmetry breaking variables
if USE_SYMMETRY_BREAKING:   
    y = mip.addVars(D,R, vtype=GRB.INTEGER, name='firstDayInUseRack', lb=0)

# constraints
mip.addConstrs(gp.quicksum([cnt[(d,b,l,r,p)] for l in L for r in R for p in P]) == nc[(d,b)] for d in D for b in B) # 1
mip.addConstrs(gp.quicksum([cnt[(d,b,l,r,p)] for b in B]) <= c for d in D for l in L for r in R for p in P ) # 2
mip.addConstrs(cnt[(d,b,l,r,p)] <= c * h[(d,b,l,r,p)] for d in D for b in B for l in L for r in R for p in P) # 3
mip.addConstrs(h[(d,b,l,r,p)] <= cnt[(d,b,l,r,p)] for d in D for b in B for l in L for r in R for p in P) # 3
mip.addConstrs(h[(d,b,l,r,p)] * F[(d,b)] <= v[(d,r)] for d in D for b in B for l in L for r in R for p in P) # 4
mip.addConstrs(v[(d,r)] <= len(F_list) * (1-h[(d,b,l,r,p)]) + h[(d,b,l,r,p)] * F[(d,b)] for d in D for b in B for l in L for r in R for p in P) # 4
mip.addConstrs(h[(d,b,l,r,p)] * I[(d,b)] <= irr[(d,l,r,p)] for d in D for b in B for l in L for r in R for p in P) # 5
mip.addConstrs(irr[(d,l,r,p)] <= len(I_list) * (1-h[(d,b,l,r,p)]) + h[(d,b,l,r,p)] * I[(d,b)] for d in D for b in B for l in L for r in R for p in P) # 5

# Linearization constraints
mip.addConstrs(v[(d,r)] - v[(d-1,r)] <= len(F_list) * Dv[(d,r)] for d in D[1:] for r in R) # 1
mip.addConstrs(v[(d-1,r)] - v[(d,r)] <= len(F_list) * Dv[(d,r)] for d in D[1:] for r in R) # 1
mip.addConstrs(cnt[(d,b,l,r,p)] - cnt[(d-1,b,l,r,p)] <= Dcnt[(d,b,l,r,p)] for d in D[1:] for b in B for l in L for r in R for p in P) # 2
mip.addConstrs(cnt[(d-1,b,l,r,p)] - cnt[(d,b,l,r,p)] <= Dcnt[(d,b,l,r,p)] for d in D[1:] for b in B for l in L for r in R for p in P) # 2

# Simple symmetry breaking constraints
if USE_SYMMETRY_BREAKING:
    mip.addConstrs(v[(d,r)] <= len(F_list) * gp.quicksum([y[(i,r)] for i in D[d-1:]]) for d in D for r in R) # 1
    mip.addConstrs(gp.quicksum([ y[(d,r)] for d in D]) == 1 for r in R) # 2
    mip.addConstrs(y[(d,r)] <= gp.quicksum([ y[i,r-1] for i in D[:d] ]) for d in D for r in R[1:]) # 3

# Advanced symmetry breaking constraints
if USE_ADVANCED_SYMMETRY_BREAKING:
    # h can only be in use, if all beneath are in use
    mip.addConstrs((l-1) * h[(d,b,l,r,p)] <= gp.quicksum([h[(d,b,i,r,p_2)] for i in L[:l] for p_2 in P]) for d in D for b in B for l in L for r in R for p in P)

# objective function
Dcnt_obj = gp.quicksum([Dcnt[(d,b,l,r,p)] for d in D[1:] for b in B for l in L for r in R for p in P]) 
Dv_obj = gp.quicksum([Dv[(d,r)] for d in D[1:] for r in R])
h_obj = gp.quicksum([h[(d,b,l,r,p)] for d in D for b in B for l in L for r in R for p in P])
obj_fn = Dcnt_obj + Dv_obj + h_obj
mip.setObjective(obj_fn, GRB.MINIMIZE)

mip.write('model.lp')
mip.optimize()

for d in D:
    for b in B:
        for l in L:
            for r in R:
                for p in P:
                    if cnt[(d,b,l,r,p)].x > 0:
                        print(F"On D{d} for B{b} at L{l}R{r}P{p} we have {cnt[(d,b,l,r,p)].x}")


