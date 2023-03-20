from position_mip import call_model as position_model
from regime_mip import call_model as regime_model
from test_mip import call_model as test_model
from parameters import *
from save import save_to_file
from helper import NotSolvableError

# try:
#     result = regime_model()
#     save_to_file(result,file_name='regime_result') 
# except TypeError:
#     raise NotSolvableError()

result = {
    'b1': {
        'nc': {
            1: 1,
            2: 1,
            3: 1,
            4: 1,
            5: 2,
            6: 2,
            7: 2,
            8: 4,
            9: 4,
        },
        'f': {
            1: 1,
            2: 1,
            3: 1,
            4: 1,
            5: 2,
            6: 2,
            7: 2,
            8: 3,
            9: 3,
        },
        'i': {
            1: 1,
            2: 1,
            3: 1,
            4: 1,
            5: 2,
            6: 2,
            7: 2,
            8: 3,
            9: 3,
        }
    },
    'b2': {
        'nc': {
            1: 1,
            2: 2,
            3: 2,
            4: 4,
        },
        'f': {
            1: 2,
            2: 2,
            3: 1,
            4: 4,
        },
        'i': {
            1: 1,
            2: 1,
            3: 1,
            4: 1,
        }
    }
}

final_result = test_model(result)
