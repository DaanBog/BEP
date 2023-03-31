from parameters import *

def calculate_maximum_start_date(batch):   
    return NUMBER_OF_DAYS - max(PRODUCT_TYPES[batch['type']]['nc'].keys())

def get_number_of_growth_days(batch):
    return max(PRODUCT_TYPES[batch['type']]['nc'].keys())