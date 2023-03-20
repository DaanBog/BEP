import gurobipy as gp
from helper import print_model_result
from parameters import DAYS, LAYERS,RACKS,POSITIONS, CONTAINERS_PER_IRRIGATION_REGIME

def call_model(batches):
    mip = gp.Model(name = "Vertical farm schedule")

    # Define variables
    tank = mip.addVars(DAYS, RACKS, vtype = gp.GRB.INTEGER, lb=0, ub=5, name=F'tank' )
    irrigation = mip.addVars(DAYS, LAYERS,RACKS,POSITIONS, vtype = gp.GRB.INTEGER, lb=0, ub=5, name=F'Irrigation' )
    container_positions_on_day = {}
    for day in DAYS:
        container_positions_on_day[day] = {} 
        for batch in batches:
            if day in batches[batch]['nc'] :
                container_list = list(range(batches[batch]['nc'][day]))
                container_positions_on_day[day][batch] = mip.addVars(container_list,LAYERS,RACKS,POSITIONS, vtype = gp.GRB.BINARY, name=F'Position of batch {batch} on day {day}')
                mip.addConstrs(gp.quicksum([container_positions_on_day[day][batch][(containers, layer, rack, position)] for layer in LAYERS for rack in RACKS for position in POSITIONS]) == 1 for containers in range(batches[batch]['nc'][day]))

    # Define contraints
    # Per position only 15 containers may be placed
        for layer in LAYERS:
            for rack in RACKS:
                for position in POSITIONS:
                    total_containers_per_position = []
                    for batch in batches:
                        if day in batches[batch]['nc']:
                            container_list = list(range(batches[batch]['nc'][day]))
                            total_containers_per_position = total_containers_per_position + [
                                container_positions_on_day[day][batch][(container, layer, rack, position)] for container in container_list
                            ]
                    mip.addConstr(gp.quicksum(total_containers_per_position) <= CONTAINERS_PER_IRRIGATION_REGIME )
    
        for batch in container_positions_on_day[day]:
            for layer in LAYERS:
                for rack in RACKS:
                    for position in POSITIONS:
                        container_list = list(range(batches[batch]['nc'][day]))
                        # Fertillizer
                        mip.addConstrs(container_positions_on_day[day][batch][(container, layer, rack ,position)] * batches[batch]['f'][day] == tank[(day,rack)] * container_positions_on_day[day][batch][(container, layer, rack ,position)] for container in container_list)

                        # Irrigation
                        mip.addConstrs(container_positions_on_day[day][batch][(container, layer, rack ,position)] * batches[batch]['i'][day] == irrigation[(day,layer,rack,position)] * container_positions_on_day[day][batch][(container, layer, rack ,position)] for container in container_list)

                   

    # Define objective function
    obj_fn = gp.quicksum(tank) + gp.quicksum(irrigation)
    mip.setObjective(obj_fn, gp.GRB.MINIMIZE)

    # optimize 
    mip.optimize() 

    # Output 
    print_model_result(mip)