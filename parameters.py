"""
The fertillizers in batches MUST be a complete list of integers [1,...,f] where f is the maximum fertillizer. 
The Irrigation in batches MUST also be a complete list of integers [1,...,i] where i is the maximum irrigation
"""

# Physical space
RACKS = ['R1','R2','R3','R4','R5','R6','R7','R8']
LAYERS = ['L1', 'L2', 'L3', 'L4', 'L5', 'L6']
CONTAINERS_PER_RACK = 30

# Plant steps 
NUMBER_OF_DAYS_MODELLED = 20
NUMBER_OF_BATCHES = 60

MULTILAYER_ENV = {}
for day in range(NUMBER_OF_DAYS_MODELLED):
    MULTILAYER_ENV[day] = {}
    for rack_number, rack in enumerate(RACKS):
        MULTILAYER_ENV[day][rack] = {
            'FERTILLIZER': None, 
        }
        for layer_number, layer in enumerate(LAYERS):
            MULTILAYER_ENV[day][rack][layer] = {
                'IRRIGATION_1': None, # Irrigation for the first half of the positions
                'IRRIGATION_2': None, # Irrigation for the second half of the positions
            }

BATCHES = {}
for batch in range(NUMBER_OF_BATCHES):
    BATCHES[batch] = {
        'NUMBER_OF_DAYS_SEEDED': 4,
        'CONATINERS_WHEN_SEEDED': 1,
        'NUMBERS_OF_DAYS_TRANSPLANTED': 3,
        'CONTAINERS_WHEN_TRANSPLATED': 2,
        'NUMBER_OF_DAYS_SPACED': 2,
        'CONTAINERS_WHEN_SPACED': 4,
        'REGIME': {
            'is_seeded': {
                'FERTILLIZER': 1,
                'IRRIGATION': 1,
            },     
            'is_transplanted': {
                'FERTILLIZER': 2,
                'IRRIGATION': 2,
            },            
            'is_spaced': {
                'FERTILLIZER': 3,
                'IRRIGATION': 3,
            },
        },
    }

            
# Override deafualt for specific batches
BATCHES[0]['NUMBER_OF_DAYS_SEEDED'] = 3
BATCHES[0]['NUMBERS_OF_DAYS_TRANSPLANTED'] = 2
BATCHES[0]['NUMBER_OF_DAYS_SPACED'] = 1

BATCHES[0]['CONATINERS_WHEN_SEEDED'] = 1
BATCHES[0]['CONTAINERS_WHEN_TRANSPLATED'] = 2
BATCHES[0]['CONTAINERS_WHEN_SPACED'] = 4

for batch in range(NUMBER_OF_BATCHES):
    
    def set_containers_per_batch_state(batch, day, state, number_of_containers_per_state):
        BATCHES[batch][day][state] = {}
        for container_index in range(number_of_containers_per_state):
            BATCHES[batch][day][state][container_index] = {}
            for rack_number, rack in enumerate(RACKS):
                BATCHES[batch][day][state][container_index][rack] = {}
                for layer_number, layer in enumerate(LAYERS):
                    BATCHES[batch][day][state][container_index][rack][layer] = {
                        0:None,
                        1: None,
                    }

    for day in range(NUMBER_OF_DAYS_MODELLED):
        BATCHES[batch][day] = {
            'not_started': None,
            'is_seeded': None,
            'is_transplanted': None,
            'is_spaced': None,
            'is_harvested': None,
        }
        BATCHES[batch][day]['containers'] = {}
        # Set containers for batch
        set_containers_per_batch_state(batch, day, 'is_seeded_containers', BATCHES[batch]['CONATINERS_WHEN_SEEDED'])
        set_containers_per_batch_state(batch, day, 'is_transplanted_containers', BATCHES[batch]['CONTAINERS_WHEN_TRANSPLATED'])
        set_containers_per_batch_state(batch, day, 'is_spaced_containers', BATCHES[batch]['CONTAINERS_WHEN_SPACED'])