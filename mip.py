from gurobipy import Model, GRB
from parameters import *
from helper import get_racks_perspective_of_containers, get_max_fertillizer, get_max_irrigation
from model_to_easy_format import model_to_easy_format

def call_model():
    mip = Model(name = "Vertical farm schedule")

    # Definition of variables
    # VARIABLES
    # Every batch has for every day positions
    for day in range(NUMBER_OF_DAYS_MODELLED):
        for batch in BATCHES:
            for state in ['is_seeded_containers', 'is_transplanted_containers', 'is_spaced_containers']:
                for container in BATCHES[batch][day][state]:
                    for rack in BATCHES[batch][day][state][container]:
                        for layer in BATCHES[batch][day][state][container][rack]:
                            for position in BATCHES[batch][day][state][container][rack][layer]:
                                BATCHES[batch][day][state][container][rack][layer][position] = mip.addVar(
                                    name= f"B{batch} : D{day} : Container {container} : state {state} : {layer}{rack}P{position}",
                                    vtype = GRB.BINARY
                                )
        # Variables for regimes on racks and half racks per layer
        for rack_number, rack in enumerate(RACKS):
            MULTILAYER_ENV[day][rack]['FERTILLIZER'] = mip.addVar(
                name = f"D{day} : {rack} fertillizer",
                 vtype = GRB.INTEGER, lb = 1, ub = get_max_fertillizer()
            )
            for layer_number, layer in enumerate(LAYERS):
                MULTILAYER_ENV[day][rack][layer]['IRRIGATION_1'] = mip.addVar(
                    name = f"D{day} : {rack}{layer}P1 : irrigation",
                    vtype = GRB.INTEGER, lb = 1, ub = get_max_irrigation()
                )                
                MULTILAYER_ENV[day][rack][layer]['IRRIGATION_2'] = mip.addVar(
                    name = f"D{day} : {rack}{layer}P2 : irrigation",
                    vtype = GRB.INTEGER, lb = 1, ub = get_max_irrigation()
                )

    # We define integer variables that represent on what day the batch was seeded 
    for batch in BATCHES:
        for day in range(NUMBER_OF_DAYS_MODELLED):
            BATCHES[batch][day]['not_started'] = mip.addVar(name = 'day ' + str(day) + 'batch' + str(batch) + ':not started' , vtype = GRB.BINARY)
            BATCHES[batch][day]['is_seeded'] = mip.addVar(name = 'day ' + str(day) + 'batch' + str(batch) + ':is seeded' , vtype = GRB.BINARY)
            BATCHES[batch][day]['is_transplanted'] = mip.addVar(name = 'day ' + str(day) +  'batch' + str(batch) + ':is transplanted' , vtype = GRB.BINARY)
            BATCHES[batch][day]['is_spaced'] = mip.addVar(name = 'day ' + str(day) +  'batch' + str(batch) + ':is spaced' , vtype = GRB.BINARY)
            BATCHES[batch][day]['is_harvested'] = mip.addVar(name = 'day ' + str(day) +  'batch' + str(batch) + ':is harvested' , vtype = GRB.BINARY)

    # CONSTRAINTS
    # Definition of constraints
    # Must fit for all 4 stages
    # For every batch for every day only 1 state can be active
    for batch in BATCHES:
        for day in range(NUMBER_OF_DAYS_MODELLED):
            mip.addConstr(BATCHES[batch][day]['not_started'] + BATCHES[batch][day]['is_seeded'] + BATCHES[batch][day]['is_transplanted'] + BATCHES[batch][day]['is_spaced'] + BATCHES[batch][day]['is_harvested'] == 1 , name='Batch' + str(batch) + ' states must be valid')
       
    
    for batch in BATCHES:
        mip.addConstr(BATCHES[batch][0]['not_started'] + BATCHES[batch][0]['is_seeded'] == 1)
        for day in range(NUMBER_OF_DAYS_MODELLED):
            # Batches must go from seeding -> transplanted -> spaced -> harvested:
            # Not allowed to take a step back
            if day + 1 < NUMBER_OF_DAYS_MODELLED :
                mip.addConstr(BATCHES[batch][day]['not_started'] <= BATCHES[batch][day + 1]['not_started'] + BATCHES[batch][day + 1]['is_seeded'])
                mip.addConstr(BATCHES[batch][day]['is_seeded'] <= BATCHES[batch][day + 1]['is_seeded'] + BATCHES[batch][day + 1]['is_transplanted'])
                mip.addConstr(BATCHES[batch][day]['is_transplanted'] <= BATCHES[batch][day + 1]['is_transplanted'] + BATCHES[batch][day + 1]['is_spaced'])
                mip.addConstr(BATCHES[batch][day]['is_spaced'] <= BATCHES[batch][day + 1]['is_spaced'] + BATCHES[batch][day + 1]['is_harvested'])
                mip.addConstr(BATCHES[batch][day]['is_harvested'] <= BATCHES[batch][day + 1]['is_harvested'])
  
            # Batches can only make a jump after a certain set time
            if day + BATCHES[batch]['NUMBER_OF_DAYS_SPACED'] < NUMBER_OF_DAYS_MODELLED:
                mip.addConstr(BATCHES[batch][day]['is_spaced'] >= BATCHES[batch][day + BATCHES[batch]['NUMBER_OF_DAYS_SPACED']]['is_harvested'])
            if day + BATCHES[batch]['NUMBERS_OF_DAYS_TRANSPLANTED'] < NUMBER_OF_DAYS_MODELLED:
                mip.addConstr(BATCHES[batch][day]['is_transplanted'] >= BATCHES[batch][day + BATCHES[batch]['NUMBERS_OF_DAYS_TRANSPLANTED']]['is_spaced'])
            if day + BATCHES[batch]['NUMBER_OF_DAYS_SEEDED'] < NUMBER_OF_DAYS_MODELLED:
                mip.addConstr(BATCHES[batch][day]['is_seeded'] >= BATCHES[batch][day + BATCHES[batch]['NUMBER_OF_DAYS_SEEDED']]['is_transplanted'])

            # Jump must be made after a certain amount of days
            if day > 0 and day + BATCHES[batch]['NUMBER_OF_DAYS_SEEDED'] < NUMBER_OF_DAYS_MODELLED:
                mip.addConstr(BATCHES[batch][day]['is_seeded'] + BATCHES[batch][day-1]['not_started'] <= BATCHES[batch][day + BATCHES[batch]['NUMBER_OF_DAYS_SEEDED']]['is_transplanted'] + 1)
            if day > 0 and day + BATCHES[batch]['NUMBERS_OF_DAYS_TRANSPLANTED'] < NUMBER_OF_DAYS_MODELLED:
                mip.addConstr(BATCHES[batch][day]['is_transplanted'] + BATCHES[batch][day-1]['is_seeded'] <= BATCHES[batch][day + BATCHES[batch]['NUMBERS_OF_DAYS_TRANSPLANTED']]['is_spaced'] + 1)
            if day > 0 and day + BATCHES[batch]['NUMBER_OF_DAYS_SPACED'] < NUMBER_OF_DAYS_MODELLED:
                mip.addConstr(BATCHES[batch][day]['is_spaced'] + BATCHES[batch][day-1]['is_transplanted'] <= BATCHES[batch][day + BATCHES[batch]['NUMBER_OF_DAYS_SPACED']]['is_harvested'] + 1)
                
    # The total number of containers allocated in the machine must be the same as the total number of containers that should be part of the batches
    for day in range(NUMBER_OF_DAYS_MODELLED):
        for batch in BATCHES:
            # The number of containers that are allocated according to a batch must be the same as the number of containers it has allocated in the machine
            number_of_containers_according_to_batches = (
                BATCHES[batch][day]['is_seeded'] * BATCHES[batch]['CONATINERS_WHEN_SEEDED'] +
                BATCHES[batch][day]['is_transplanted'] * BATCHES[batch]['CONTAINERS_WHEN_TRANSPLATED'] + 
                BATCHES[batch][day]['is_spaced'] * BATCHES[batch]['CONTAINERS_WHEN_SPACED'] 
            ) 

            number_of_containers_according_to_ml_locations = 0 

            for state in ['is_seeded_containers', 'is_transplanted_containers', 'is_spaced_containers']:
                for container in BATCHES[batch][day][state]:
                    container_allocations = 0
                    for rack in BATCHES[batch][day][state][container]:
                        for layer in BATCHES[batch][day][state][container][rack]:
                            for position in BATCHES[batch][day][state][container][rack][layer]:
                                number_of_containers_according_to_ml_locations += BATCHES[batch][day][state][container][rack][layer][position] * BATCHES[batch][day][state.replace("_containers", "")]
                                container_allocations += BATCHES[batch][day][state][container][rack][layer][position] * BATCHES[batch][day][state.replace("_containers", "")]
                                if state == 'is_seeded_containers':
                                    # Containers that have not been seeded do not appear in the multilayer
                                    mip.addConstr(BATCHES[batch][day][state][container][rack][layer][position] * BATCHES[batch][day]['not_started'] == 0)
                                # Fertillizer must match
                                mip.addConstr(BATCHES[batch][day][state][container][rack][layer][position] * ( BATCHES[batch]['REGIME'][state.replace("_containers", "")]['FERTILLIZER'] - MULTILAYER_ENV[day][rack]['FERTILLIZER'] ) == 0 )
                                # Irrigation must match
                                mip.addConstr(BATCHES[batch][day][state][container][rack][layer][position] * ( BATCHES[batch]['REGIME'][state.replace("_containers", "")]['IRRIGATION'] - MULTILAYER_ENV[day][rack][layer]['IRRIGATION_' + str(position + 1)]) == 0 )
                    mip.addConstr(container_allocations <= 1, name=F'Container{container} must be allocated once')
       
            mip.addConstr(number_of_containers_according_to_batches == number_of_containers_according_to_ml_locations, name=F'day {day} total number of containers match for batch {batch}')
            
        # For every day, the total number of containers in a half position of a rack is at most c/2
        for rack_number, rack in enumerate(RACKS):
            for layer_number, layer in enumerate(LAYERS):
                for position in [0,1]:
                    total_number_of_containers_in_this_half_rack = 0
                    for batch in BATCHES:
                        for state in ['is_seeded_containers', 'is_transplanted_containers', 'is_spaced_containers']:
                            for container in BATCHES[batch][day][state]:
                                total_number_of_containers_in_this_half_rack += BATCHES[batch][day][state][container][rack][layer][position] * BATCHES[batch][day][state.replace("_containers", "")]
                    mip.addConstr(total_number_of_containers_in_this_half_rack <= CONTAINERS_PER_RACK / 2)

    # On the final day, all batches must be harvested
    harvested_batches = 0
    for batch in BATCHES:
        harvested_batches += BATCHES[batch][NUMBER_OF_DAYS_MODELLED - 1]['is_harvested']
    mip.addConstr(harvested_batches == NUMBER_OF_BATCHES, name=F"B{batch}_harvested_on_final_day")

    # OBJECTIVE FUNCTION

    # Definition of objective function
    obj_fn = 0
    # As little movements as possible, i.e., when something is at some place on day 1, it may still be there on day 2 also switching of fertillizer or irrigation
    for day in range(NUMBER_OF_DAYS_MODELLED - 1):
        for batch in BATCHES:
            for rack_number, rack in enumerate(RACKS):
                for layer_number, layer in enumerate(LAYERS):
                    for position in [0,1]:
                        for state in ['is_seeded_containers', 'is_transplanted_containers', 'is_spaced_containers']:
                            for container in BATCHES[batch][day][state]:
                                obj_fn += (BATCHES[batch][day + 1][state][container][rack][layer][position] - BATCHES[batch][day + 1][state][container][rack][layer][position] )
    
    mip.setObjective(obj_fn, GRB.MAXIMIZE)


    # Call solver
    mip.optimize() 
    return (model_to_easy_format())

    

