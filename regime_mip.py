from gurobipy import Model, GRB
from parameters import *


def call_model():
    mip = Model(name = "Vertical farm schedule")

    # Definition of variables
    
    # Definition of constraints
   
    # Definition of objective function
    obj_fn = 0


    mip.setObjective(obj_fn, GRB.MINIMIZE)

    # Call solver
    mip.optimize() 
    

    

