
"""
From full name to abbreviation
+--------------+--------------+
|     Name     | Abbreviation |
+--------------+--------------+
| not_seeded   | ns           |
| seeded       | se           |
| transplanted | t            |
| spaced       | sp           |
| harvested    | h            |
| # containers | nc           |
| # days       | nd           |
| irrigation   | i            |
| fertillizer  | f            |
+--------------+--------------+

For allocations:
    it is important that any irrigation has a 1 to 1 relation to a fertillizer. so if we have batch 1 that when seeded needs f1 and i1, then any batch at any point that does not use f1 cannot use i1
"""

# Physical space
RACKS = ['R1','R2','R3','R4','R5','R6','R7','R8']
LAYERS = ['L1', 'L2', 'L3', 'L4', 'L5', 'L6']
CONTAINERS_PER_RACK = 30
SECTIONS_PER_RACK_LAYER = 2
POSITIONS = list(map( lambda x: f"P{x}",list(range(SECTIONS_PER_RACK_LAYER))))
# Modelling paramaters
NUMBER_OF_DAYS = 10

# Both fertillizer and irrigation must not have any gaps, so the total list of all those scripts must be [1,2,...,n]
TANKS_REGIMES = [1,2,3]
IRRIGATION_REGIMES = {1:1, 2:2, 3:3}

IRRIGATION_REGIMES_PER_RACK = len(LAYERS) * SECTIONS_PER_RACK_LAYER
CONTAINERS_PER_IRRIGATION_REGIME = CONTAINERS_PER_RACK / SECTIONS_PER_RACK_LAYER

STATES = ['ns', 'se', 't', 'sp', 'h']
STATES_WITH_CONTAINERS = ['se', 't', 'sp']
BATCHES = {
    'b1':{
        'nc':{
            'se': 1,
            't': 2,
            'sp': 4,
        },
        'nd':{
            'se': 3,
            't': 2,
            'sp': 2,    
        },
        'i':{
            'se': 1,
            't': 2,
            'sp': 3,    
        },
        'f':{
            'se': 1,
            't': 2,
            'sp': 3,    
        },

    },
    # 'b2':{
    #     'nc':{
    #         'se': 40,
    #         't': 80,
    #         'sp': 120,
    #     },
    #     'nd':{
    #         'se': 3,
    #         't': 2,
    #         'sp': 2,    
    #     },
    #     'i':{
    #         'se': 1,
    #         't': 2,
    #         'sp': 3,    
    #     },
    #     'f':{
    #         'se': 1,
    #         't': 2,
    #         'sp': 3,    
    #     },
    # },
}

DAYS = list(range(NUMBER_OF_DAYS)) 
