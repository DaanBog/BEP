from parameters import *

class NotSolvableError(Exception):
    "MIP could not be solved, no solution is possible"
    pass

def get_max_fertillizer(batches_info):
    return max([batches_info[batch]['f'][state] for batch in batches_info for state in ['se', 't', 'sp']])

def get_max_irrigation(batches_info):
    return max([batches_info[batch]['i'][state] for batch in batches_info for state in ['se', 't', 'sp']])

def next_day(day):
    days_keys = list(DAYS)
    next_day = days_keys[days_keys.index(day) + 1]
    return next_day

def get_previous_day(day):
    days_keys = list(DAYS)
    previous = days_keys[days_keys.index(day) - 1]
    return previous

def get_first_day():
    days_keys = list(DAYS)
    first_day = days_keys[0]
    return first_day

def get_last_day():
    days_keys = list(DAYS)
    last_day = days_keys[-1]
    return last_day

def get_day_numeric(day):
    days_keys = list(DAYS)
    day_index = days_keys.index(day)
    return day_index

def print_model_result(mip):
    for v in mip.getVars():
        if v.x != 0:
            print ('%s: %g' % (v.varName, v.x))

def save_model_to_file(file_name, model):
    model.write(F"{file_name}.lp")