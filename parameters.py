
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
"""

# Physical space
RACKS = ['R1','R2','R3','R4','R5','R6','R7','R8']
LAYERS = ['L1', 'L2', 'L3', 'L4', 'L5', 'L6']
CONTAINERS_PER_RACK = 30
SECTIONS_PER_RACK_LAYER = 2

# Modelling paramaters
NUMBER_OF_DAYS = 9
BATCHES = {
    'b1':{
        'nc':{
            'se': 1,
            't': 2,
            'sp': 4,
        },
        'nd':{
            'se': 4,
            't': 3,
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
}
