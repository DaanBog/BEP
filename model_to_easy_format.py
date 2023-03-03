from parameters import BATCHES, NUMBER_OF_DAYS_MODELLED, MULTILAYER_ENV

class InvalidSolution(Exception):
    "The returned solution was not valid"
    pass

def get_batch_state(batch):
    if batch['not_started'].x > 0:
        return 'not_started'
    elif batch['is_seeded'].x > 0:
        return 'is_seeded'    
    elif batch['is_transplanted'].x > 0:
        return 'is_transplanted'    
    elif batch['is_spaced'].x > 0:
        return 'is_spaced'    
    elif batch['is_harvested'].x > 0:
        return 'is_harvested'
    raise InvalidSolution("Batch has no state")

def get_container_position(container_data):
    for rack in container_data:
        for layer in container_data[rack]:
            for position in container_data[rack][layer]:
                if container_data[rack][layer][position].x > 0:
                    return layer, rack, position
    raise InvalidSolution("Container not allocated")

def model_to_easy_format():
    result = {}
    ENV = {}
    for day in range(NUMBER_OF_DAYS_MODELLED):
        day_result_key = F"D{day}"
        result[day_result_key] = {}
        for batch in BATCHES:
            batch_result_key = F"B{batch}"
            state =  get_batch_state(BATCHES[batch][day])
            result[day_result_key][batch_result_key] = {
                'state': state,
            }
            if state in ['is_seeded', 'is_transplanted', 'is_spaced']:
                result[day_result_key][batch_result_key]['containers'] = {}
                containers_key = result[day_result_key][batch_result_key]['state'] + '_containers'
                for container in BATCHES[batch][day][containers_key]:
                    layer, rack, position = get_container_position(BATCHES[batch][day][containers_key][container])
                    container_key = F"C{container}"
                    result[day_result_key][batch_result_key]['containers'][container_key] = {
                        'layer': layer,
                        'rack': rack,
                        'position': position,
                    }
            else:
                continue
        
        ENV[day] = {}
        for rack in MULTILAYER_ENV[day]:
            ENV[day][rack] = {'fertillizer' : int(MULTILAYER_ENV[day][rack]['FERTILLIZER'].x)}
            for layer in MULTILAYER_ENV[day][rack]:
                if layer == 'FERTILLIZER':
                    continue
                ENV[day][rack][layer] = {
                    'irrigation_1': int(MULTILAYER_ENV[day][rack][layer]['IRRIGATION_1'].x),
                    'irrigation_2': int(MULTILAYER_ENV[day][rack][layer]['IRRIGATION_2'].x),
                }
                
    return result, ENV
