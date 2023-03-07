from gurobipy import Model, GRB
from parameters import *


def call_model():
    mip = Model(name = "Vertical farm schedule")

    # Definition of variables
    tanks = mip.addVars(RACKS, lb=0, ub=10,  vtype = GRB.INTEGER)
    irrigation = mip.addVars(LAYERS, RACKS, [0,1], lb=0, ub=10, vtype = GRB.INTEGER )
    print(irrigation.valuess)
   
   
    # Definition of constraints
   
    # Definition of objective function
    obj_fn = 0


    mip.setObjective(obj_fn, GRB.MINIMIZE)

    # Call solver
    mip.optimize() 
    

    

