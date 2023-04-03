from mip import *
from parameters import *

mip = Model(sense=MAXIMIZE, solver_name=GRB) # Change solver to GRB for Gurobi solver, CBC for free solver
           
containers_per_day_per_batch = {}
batch_is_allocated_at_pos = {}
tanks = {}
irrigation = {}

for day in DAYS:
    # Set tanks
    tanks[day] = { rack : mip.add_var(var_type=INTEGER, lb=0, ub=max(FERTILLIZERS), name=F"D{day}_Tank_at_R{rack}") for rack in RACKS  }

    # Set irrigation
    irrigation[day] = {}
    for layer in LAYERS:
        irrigation[day][layer] = {}
        for rack in RACKS:
            irrigation[day][layer][rack] = {}
            for position in POSITIONS:
                irrigation[day][layer][rack][position] = mip.add_var(var_type=INTEGER, lb=0, ub=max(IRRIGATION_SCRIPTS), name=F"D{day}_irrigation_at_L{layer}R{rack}P{position}")

    # Set positions
    containers_per_day_per_batch[day] = {}
    batch_is_allocated_at_pos[day] = {}
    for batch in BATCHES:
        if day in BATCHES[batch]['nc']:
            # Per half rack per layer we have a variable that stores how many containers on there are on this day of this batch
            containers_per_day_per_batch[day][batch] = { (layer,rack,position) : mip.add_var(var_type=INTEGER, lb=0, ub=NUMBER_OF_CONTAINERS_PER_POSITION, name=F"nc_at_D{day}_B{batch}_L{layer}_R{rack}_P{position}") for layer in LAYERS for rack in RACKS for position in POSITIONS }
            batch_is_allocated_at_pos[day][batch] = { (layer,rack,position) : mip.add_var(var_type=BINARY, name=F"batch_allocated_at_D{day}_B{batch}_L{layer}_R{rack}_P{position}") for layer in LAYERS for rack in RACKS for position in POSITIONS }
            # exactly 'nc' containers must be seeded on this 
            mip += xsum([ containers_per_day_per_batch[day][batch][(layer,rack,position)] for layer in LAYERS for rack in RACKS for position in POSITIONS ]) == BATCHES[batch]['nc'][day]
            
    for layer in LAYERS:
        for rack in RACKS:
            for position in POSITIONS:
                # only 15 containers can be in a
                mip += xsum([ containers_per_day_per_batch[day][batch][(layer,rack,position)] for batch in containers_per_day_per_batch[day] ]) <= NUMBER_OF_CONTAINERS_PER_POSITION
                for batch in containers_per_day_per_batch[day]:
                    # Link number of containers to batches being allocated
                    mip += containers_per_day_per_batch[day][batch][(layer,rack,position)] <= NUMBER_OF_CONTAINERS_PER_POSITION * batch_is_allocated_at_pos[day][batch][(layer,rack,position)]
                    mip += batch_is_allocated_at_pos[day][batch][(layer,rack,position)] <= containers_per_day_per_batch[day][batch][(layer,rack,position)]
                    # Tank must match 
                    mip += batch_is_allocated_at_pos[day][batch][(layer,rack,position)] * BATCHES[batch]['f'][day] <= tanks[day][rack]
                    mip += tanks[day][rack] <= (1-batch_is_allocated_at_pos[day][batch][(layer,rack,position)]) * max(FERTILLIZERS) + batch_is_allocated_at_pos[day][batch][(layer,rack,position)] * BATCHES[batch]['f'][day]
                    # Irrigation must match
                    mip += batch_is_allocated_at_pos[day][batch][(layer,rack,position)] * BATCHES[batch]['i'][day] <= irrigation[day][layer][rack][position]
                    mip += irrigation[day][layer][rack][position] <= (1-batch_is_allocated_at_pos[day][batch][(layer,rack,position)]) * max(IRRIGATION_SCRIPTS) + batch_is_allocated_at_pos[day][batch][(layer,rack,position)] * BATCHES[batch]['i'][day]

mip.objective = minimize(xsum([tanks[day][rack] for day in DAYS for rack in RACKS ]))     

mip.write('model.lp')
mip.optimize(max_seconds=300)

for v in mip.vars:
    if abs(v.x) > 1e-6: # only printing non-zeros
        print('{} : {}'.format(v.name, v.x))
