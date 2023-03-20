from gurobipy import Model, GRB
from parameters import DAYS, LAYERS, RACKS, POSITIONS, CONTAINERS_PER_IRRIGATION_REGIME, STATES_WITH_CONTAINERS, BATCHES
import gurobipy as gp
from helper import print_model_result, save_model_to_file

def call_model(batches):
    mip = Model(name = "Vertical farm schedule")

    batches_keys = batches.keys()

    add_containers_to_batches(batches)
    # Definition of variables
    locations = {}
    for day in DAYS:
        locations[day] = {}
        for batch in batches_keys:
            locations[day][batch] = {}
            try:
                locations[day][batch] = mip.addVars(list(batches[batch]['containers'][day].keys()) ,LAYERS, RACKS, POSITIONS, name=F"position_of_{batch}_on_{day}", vtype=GRB.BINARY)
            except KeyError:
                pass # When a key error is raised, it it because a day has no containers, then we do not add new locations for this batch

    # Definition of constraints
    # total number of containers per day should be the same 
    for day in DAYS:
        total_number_of_containers_according_to_positions = 0
        for batch in batches_keys:
            try:
                total_number_of_containers_according_to_positions += gp.quicksum(locations[day][batch])
            except KeyError:
                pass
        mip.addConstr((total_number_of_containers_on_day(day, batches) == total_number_of_containers_according_to_positions), name=F"{day} number_of_containers_match")
   
        # Every container is allocated
        for batch in batches_keys:
            try: 
                mip.addConstrs(1 == gp.quicksum([locations[day][batch][(c, layer, rack, position)] for layer in LAYERS for rack in RACKS for position in POSITIONS]) for c in list(batches[batch]['containers'][day].keys()))
            except KeyError:
                pass

        # Total number of allocated containers on position <= 15
        # TODO

        # If container allocated on position, irrigation matches
        # TODO

        # if container allocated on position, tank matches
        # TODO



    # Definition of objective function
    obj_fn = 0


    mip.setObjective(obj_fn, GRB.MINIMIZE)
    save_model_to_file('position_model', mip)
    # Call solver
    mip.optimize() 
    print_model_result(mip)
    

def total_number_of_containers_on_day(day, batches):
    total_number_of_containers = 0
    for batch in batches:
        if batches[batch]['planning'][day] in STATES_WITH_CONTAINERS:  
            total_number_of_containers += batches[batch]['nc'][batches[batch]['planning'][day]]

    return total_number_of_containers

def add_containers_to_batches(batches):
    for batch in batches:
        batches[batch]['containers'] = {}
        for day in DAYS:
            nc = 0
            if batches[batch]['planning'][day] in STATES_WITH_CONTAINERS:  
                nc = batches[batch]['nc'][batches[batch]['planning'][day]]
                batches[batch]['containers'][day] = {}
                for c in range(nc):
                    c_key = F"C{c + 1}"
                    batches[batch]['containers'][day][c_key] = None
