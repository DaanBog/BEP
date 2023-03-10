from gurobipy import Model, GRB
from parameters import DAYS, LAYERS, RACKS, POSITIONS, CONTAINERS_PER_IRRIGATION_REGIME, STATES_WITH_CONTAINERS, BATCHES
import gurobipy as gp

def call_model(batches):
    mip = Model(name = "Vertical farm schedule")

    batches_keys = BATCHES.keys()

    # Definition of variables
    locations = mip.addVars(DAYS, batches_keys, LAYERS, RACKS, POSITIONS, name="position per day", vtype=GRB.INTEGER, lb=0, ub=CONTAINERS_PER_IRRIGATION_REGIME)

    # Definition of constraints
    # total number of containers per day should be the same 
    mip.addConstrs(total_number_of_containers_on_day(day, batches) == gp.quicksum([locations[(day,batch,layer,rack,position)] for batch in batches_keys for layer in LAYERS for rack in RACKS for position in POSITIONS]) for day in DAYS)
   
    # Definition of objective function
    obj_fn = 0


    mip.setObjective(obj_fn, GRB.MINIMIZE)

    # Call solver
    mip.optimize() 
    

def total_number_of_containers_on_day(day, batches):
    total_number_of_containers = 0
    for batch in batches:
        if batches[batch]['planning'][day] in STATES_WITH_CONTAINERS:  
            total_number_of_containers += batches[batch]['nc'][batches[batch]['planning'][day]]

    return total_number_of_containers

