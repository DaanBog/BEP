from pyscipopt import Model

from parameters import *

mip = Model(sense=MAXIMIZE, solver_name=GRB) # Change solver to GRB for Gurobi solver, CBC for free solver


USE_SYMMETRY_BREAKER = False

containers_per_day_per_batch = {}
batch_is_allocated_at_pos = {}
batch_has_changed_position = {}
tanks = {}
tanks_first_day = {}
tanks_has_changed = {}
irrigation = {}

for day in DAYS:
    # Set tanks
    tanks[day] = { rack : mip.add_var(var_type=INTEGER, lb=0, ub=max(FERTILLIZERS), name=F"D{day}_Tank_at_R{rack}") for rack in RACKS  }
    if USE_SYMMETRY_BREAKER:
        tanks_first_day[day] = { rack : mip.add_var(var_type=BINARY, name=F"R{rack}_first_day_D{day}") for rack in RACKS  }
    
    if day > 1:
        tanks_has_changed[day] = { rack: mip.add_var(var_type=BINARY) for rack in RACKS}
        for rack in RACKS:
            mip += tanks[day][rack] - tanks[day - 1][rack] <= max(FERTILLIZERS) * tanks_has_changed[day][rack]
            mip += tanks[day - 1][rack] - tanks[day][rack] <= max(FERTILLIZERS) * tanks_has_changed[day][rack]
            
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
    if day > 1:
        batch_has_changed_position[day] = {}
    for batch in BATCHES:
        if day in BATCHES[batch]['nc']:
            # Per half rack per layer we have a variable that stores how many containers on there are on this day of this batch
            containers_per_day_per_batch[day][batch] = { (layer,rack,position) : mip.add_var(var_type=INTEGER, lb=0, ub=NUMBER_OF_CONTAINERS_PER_POSITION, name=F"nc_at_D{day}_B{batch}_L{layer}_R{rack}_P{position}") for layer in LAYERS for rack in RACKS for position in POSITIONS }
            batch_is_allocated_at_pos[day][batch] = { (layer,rack,position) : mip.add_var(var_type=BINARY, name=F"batch_allocated_at_D{day}_B{batch}_L{layer}_R{rack}_P{position}") for layer in LAYERS for rack in RACKS for position in POSITIONS }
            if day > 1 and day-1 in BATCHES[batch]['nc'] and BATCHES[batch]['nc'][day] == BATCHES[batch]['nc'][day-1]:
                batch_has_changed_position[day][batch] = {(layer,rack,position) : mip.add_var(var_type=INTEGER, lb=0, ub=BATCHES[batch]['nc'][day], name=F"Batch_{batch}_changed_position_at_D{day}") for layer in LAYERS for rack in RACKS for position in POSITIONS }
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

# Now keep track of changes and optimize on that 
for day in DAYS:
    if day <= 1:
        continue
    for batch in batch_has_changed_position[day]:
        for layer in LAYERS:
            for rack in RACKS:
                for position in POSITIONS:
                    mip += containers_per_day_per_batch[day][batch][(layer,rack,position)] -  containers_per_day_per_batch[day - 1][batch][(layer,rack,position)] <= batch_has_changed_position[day][batch][(layer,rack,position)]
                    mip += -containers_per_day_per_batch[day][batch][(layer,rack,position)] +  containers_per_day_per_batch[day - 1][batch][(layer,rack,position)] <= batch_has_changed_position[day][batch][(layer,rack,position)]
                    if USE_SYMMETRY_BREAKER:
                        mip += containers_per_day_per_batch[day][batch][(layer,rack,position)] <= NUMBER_OF_CONTAINERS_PER_POSITION * xsum([tanks_first_day[day][rack] for day in DAYS[:day]])

if USE_SYMMETRY_BREAKER:
    for rack in RACKS:
        # Only 1 day can be the first day!
        mip += xsum([tanks_first_day[day][rack] for day in DAYS]) == 1 


tanks_sum = xsum([tanks[day][rack] for day in DAYS for rack in RACKS ])
changed_tank_sum = xsum([tanks_has_changed[day][rack] for day in tanks_has_changed for rack in tanks_has_changed[day]])
irrigation_sum =  xsum([irrigation[day][layer][rack][position] for day in DAYS for layer in LAYERS for rack in RACKS for position in POSITIONS])
changes_positions_sum = xsum([ batch_has_changed_position[day][batch][index] for day in batch_has_changed_position for batch in batch_has_changed_position[day] for index in batch_has_changed_position[day][batch]])

mip.objective = minimize(tanks_sum + irrigation_sum + changes_positions_sum + changed_tank_sum)     

mip.write('model.lp')
mip.optimize()

# for v in mip.vars:
#     if abs(v.x) > 1e-6: # only printing non-zeros
#         print('{} : {}'.format(v.name, v.x))

for day in DAYS:
    for batch in containers_per_day_per_batch[day]:
        for layer in LAYERS:
            for rack in RACKS:
                for position in POSITIONS:
                    if containers_per_day_per_batch[day][batch][(layer,rack,position)].x > 0:
                        print(F"D{day}: batch {batch} is at L{layer}R{rack}P{position} = {containers_per_day_per_batch[day][batch][(layer,rack,position)].x}")