FILE_NAME = 'result'
import json

def save_to_file(result, file_name = FILE_NAME):
    with open(F'results/{file_name}.txt', 'w') as result_file:
            result_file.write(json.dumps(result))
