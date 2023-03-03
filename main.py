from mip import call_model
from parameters import *
from save import save_to_file

result, ENV = call_model()
# combined_result = {'result': result, 'ENV': ENV}
# save_to_file(combined_result)
save_to_file(result,file_name='result')
save_to_file(ENV,file_name='env')