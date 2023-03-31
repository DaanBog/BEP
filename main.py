from mip import *
from parameters import *
from helpers import *

mip = Model(sense=MAXIMIZE, solver_name=CBC) # Change solver to GRB for Gurobi solver, CBC for free solver

CONTAINERS = {}
TANKS = {}
IRRIGATION = {}
for day in DAYS:
    TANKS[day] = {}
    IRRIGATION[day] = {}
    for rack in RACKS:
        TANKS[day][rack] = {}
        for fertillizer in FERTILLIZERS:
            TANKS[day][rack][fertillizer] = mip.add_var(
                var_type=BINARY,
                #name=F"D{day}:F{fertillizer}:at-R{rack}"
            )
        mip += xsum([TANKS[day][rack][fertillizer] for fertillizer in FERTILLIZERS]) <= 1

    for layer in LAYERS:
        IRRIGATION[day][layer] = {}
        for rack in RACKS:
            IRRIGATION[day][layer][rack] = {}
            for position in POSITIONS:
                IRRIGATION[day][layer][rack][position] = {}
                for irrigation in IRRIGATION_SCRIPTS:
                    IRRIGATION[day][layer][rack][position][irrigation] = mip.add_var(
                        var_type=BINARY,
                       # name=F"D{day}:I{irrigation}:at-L{layer}R{rack}P{position}"
                    )
                mip += xsum([IRRIGATION[day][layer][rack][position][irrigation] for irrigation in IRRIGATION_SCRIPTS]) <= 1

    CONTAINERS[day] = {}
    for batch_index, batch in enumerate(BATCHES):
        if day in BATCHES[batch]['nc']:
            CONTAINERS[day][batch] = {} 
            for container in range(BATCHES[batch]['nc'][day]):
                CONTAINERS[day][batch][container] = {(layer,rack,position): mip.add_var(
                        var_type=BINARY,
                        #name=F"D{day}:B{batch_index}C{container}:at-L{layer}R{rack}P{position}",
                    )
                    for layer in LAYERS
                    for rack in RACKS
                    for position in POSITIONS
                }
                # A container is always precisely in 1 position
                mip += xsum([CONTAINERS[day][batch][container][(layer,rack,position)] for layer in LAYERS for rack in RACKS for position in POSITIONS]) == 1   
                for layer in LAYERS:
                    for rack in RACKS:
                        for position in POSITIONS:
                            # Fertillizer must match
                            mip += CONTAINERS[day][batch][container][(layer,rack,position)] <= TANKS[day][rack][BATCHES[batch]['f'][day]]
                            # Irrigation must match
                            mip += CONTAINERS[day][batch][container][(layer,rack,position)] <= IRRIGATION[day][layer][rack][position][BATCHES[batch]['i'][day]]

            # A position can have a maximum of 15 containers
    for layer in LAYERS:
        for rack in RACKS:
            for position in POSITIONS:
                mip += xsum([CONTAINERS[day][batch][container][(layer,rack,position)] for batch in CONTAINERS[day] for container in CONTAINERS[day][batch]]) <= NUMBER_OF_CONTAINERS_PER_POSITION
                           
                      

Fertillizer_sum = xsum([TANKS[day][rack][fertillizer] for day in DAYS for rack in RACKS for fertillizer in FERTILLIZERS]) 
irrigation_sum = xsum([IRRIGATION[day][layer][rack][position][script] for day in DAYS for layer in LAYERS for rack in RACKS for position in POSITIONS for script in IRRIGATION_SCRIPTS])
mip.objective = minimize(Fertillizer_sum + irrigation_sum) 

mip.write('model.lp')
mip.optimize(max_seconds=300)

for v in mip.vars:
    if abs(v.x) > 1e-6: # only printing non-zeros
        print('{} : {}'.format(v.name, v.x))