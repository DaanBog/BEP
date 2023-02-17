from parameters import BATCHES

def get_racks_perspective_of_containers():
    raise NotImplementedError("TODO")

def get_max_fertillizer():
    return max([BATCHES[batch]['REGIME'][state]['FERTILLIZER']for state in ['is_seeded', 'is_transplanted', 'is_spaced'] for batch in BATCHES])

def get_max_irrigation():
    return max([BATCHES[batch]['REGIME'][state]['IRRIGATION']for state in ['is_seeded', 'is_transplanted', 'is_spaced'] for batch in BATCHES])