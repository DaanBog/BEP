from position_mip import call_model as position_model
from regime_mip import call_model as regime_model
from parameters import *
from save import save_to_file
from helper import NotSolvableError

try:
    result = regime_model()
    save_to_file(result,file_name='result') 
except TypeError:
    raise NotSolvableError()