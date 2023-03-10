from gurobipy import Model, GRB
import gurobipy as gp
from helper import get_max_fertillizer, get_max_irrigation, next_day, get_first_day, get_day_numeric, get_last_day, get_previous_day, NotSolvableError
from parameters import *

def call_model():
    mip = Model(name = "Vertical farm schedule")

    # Definition of variables
    # allocations
    tanks = mip.addVars(DAYS, TANKS_REGIMES, lb=0, ub=len(RACKS), vtype = GRB.INTEGER, name='tank')
    irrigation = mip.addVars(DAYS, IRRIGATION_REGIMES, lb=0, ub=len(RACKS) * len(LAYERS) * SECTIONS_PER_RACK_LAYER, vtype = GRB.INTEGER, name='irrigation' )
    
    # batches
    batches_keys = BATCHES.keys()
    batches_states = mip.addVars(DAYS,batches_keys,STATES, vtype = GRB.BINARY, name='batch is state on day')

    # Definition of constraints

    # Maximum tank allocation
    mip.addConstrs(gp.quicksum([tanks[(day,regime)] for regime in TANKS_REGIMES]) <= len(RACKS) for day in DAYS)
    
    # Maximum irrigation allocation
    mip.addConstrs(gp.quicksum([irrigation[(day, regime)] for regime in IRRIGATION_REGIMES]) <= len(RACKS) * len(LAYERS) * SECTIONS_PER_RACK_LAYER for day in DAYS)

    # For every day, only so many irrigation of a type can be allocated if it has an allocated fertillizer
    mip.addConstrs(gp.quicksum([irrigation[(day,regime)]]) <= IRRIGATION_REGIMES_PER_RACK * tanks[(day,IRRIGATION_REGIMES[regime])] for day in DAYS for regime in IRRIGATION_REGIMES )

    # On day 1, every batch is either not started or seeded
    mip.addConstrs(batches_states[(get_first_day(), batch, 'ns')] + batches_states[(get_first_day(), batch, 'se')] == 1 for batch in batches_keys)

    # Every batch is in 1 state per day
    mip.addConstrs(batches_states[(day,batch,'ns')] + batches_states[(day,batch,'se')] + batches_states[(day,batch,'t')] + batches_states[(day,batch,'sp')] + batches_states[(day,batch,'h')]   == 1 for day in DAYS for batch in batches_keys)

    # A batch can only go through states in the order ns -> se -> t -> sp -> h
    mip.addConstrs(batches_states[(day,batch,'ns')] <= batches_states[(next_day(day),batch,'ns')] + batches_states[(next_day(day),batch,'se')] for day in DAYS[:-1] for batch in batches_keys)
    mip.addConstrs(batches_states[(day,batch,'se')] <= batches_states[(next_day(day),batch,'se')] + batches_states[(next_day(day),batch,'t')] for day in DAYS[:-1] for batch in batches_keys)
    mip.addConstrs(batches_states[(day,batch,'t')] <= batches_states[(next_day(day),batch,'t')] + batches_states[(next_day(day),batch,'sp')] for day in DAYS[:-1] for batch in batches_keys)
    mip.addConstrs(batches_states[(day,batch,'sp')] <= batches_states[(next_day(day),batch,'sp')] + batches_states[(next_day(day),batch,'h')] for day in DAYS[:-1] for batch in batches_keys)
    mip.addConstrs(batches_states[(day,batch,'h')] <= batches_states[(next_day(day),batch,'h')] for day in DAYS[:-1] for batch in batches_keys)

    # batches can only jump after a certain set time
    for batch in batches_keys:
        for day in DAYS:
            day_numeric = get_day_numeric(day)
            if day_numeric + BATCHES[batch]['nd']['sp'] < NUMBER_OF_DAYS:
                mip.addConstr(batches_states[(day,batch,'sp')] >= batches_states[(DAYS[day_numeric + BATCHES[batch]['nd']['sp']],batch,'h')])
            if day_numeric + BATCHES[batch]['nd']['t'] < NUMBER_OF_DAYS:
                mip.addConstr(batches_states[(day,batch,'t')] >= batches_states[(DAYS[day_numeric + BATCHES[batch]['nd']['t']],batch,'sp')])
            if day_numeric + BATCHES[batch]['nd']['se'] < NUMBER_OF_DAYS:
                mip.addConstr(batches_states[(day,batch,'se')] >= batches_states[(DAYS[day_numeric + BATCHES[batch]['nd']['se']],batch,'t')])

    # Batches must have jumped after a certain set time 
            if day_numeric > 0 and day_numeric + BATCHES[batch]['nd']['se'] < NUMBER_OF_DAYS:
                mip.addConstr(batches_states[(day,batch,'se')] + batches_states[(get_previous_day(day), batch, 'ns')] <= batches_states[(DAYS[day_numeric + BATCHES[batch]['nd']['se']],batch,'t')] + 1 )
            if day_numeric > 0 and day_numeric +  BATCHES[batch]['nd']['t'] < NUMBER_OF_DAYS:
                mip.addConstr(batches_states[(day,batch,'t')] + batches_states[(get_previous_day(day), batch, 'se')] <= batches_states[(DAYS[day_numeric + BATCHES[batch]['nd']['t']],batch,'sp')] + 1 )
            if day_numeric > 0 and day_numeric + BATCHES[batch]['nd']['sp'] < NUMBER_OF_DAYS:
                mip.addConstr(batches_states[(day,batch,'sp')] + batches_states[(get_previous_day(day), batch, 't')] <= batches_states[(DAYS[day_numeric + BATCHES[batch]['nd']['sp']],batch,'h')] + 1 )

    # An allocated batch needs a certain amount of containers to be available
    mip.addConstrs(batches_states[(day,batch,state)] * BATCHES[batch]['nc'][state] <= CONTAINERS_PER_IRRIGATION_REGIME * irrigation[(day,BATCHES[batch]['i'][state])] for day in DAYS for batch in batches_keys for state in STATES_WITH_CONTAINERS)

    # On the final day, every batch must be harvested
    mip.addConstrs(batches_states[(get_last_day(), batch, 'h')] == 1 for batch in batches_keys)

    # Definition of objective function
    obj_fn = gp.quicksum(tanks) + gp.quicksum(irrigation)

    mip.setObjective(obj_fn, GRB.MINIMIZE)

    # Call solver
    save_model_to_file("regime_model", mip)
    mip.write("regime_model.lp")
    mip.optimize() 
    return model_to_json(batches_states)
 

def model_to_json(batches):
    final_batches_planning = BATCHES
    for batch in BATCHES:
        final_batches_planning[batch]["planning"] = {}
        # extract final planning from model
        for day in DAYS:
            final_batches_planning[batch]["planning"][day] = get_state_of_batch_on_day_from_model(batch,day,batches)
    return final_batches_planning

def save_model_to_file(file_name, model):
    model.write(F"{file_name}.lp")

def print_model_result(mip):
    for v in mip.getVars():
        if v.x != 0:
            print ('%s: %g' % (v.varName, v.x))

def get_state_of_batch_on_day_from_model(batch, day, batches_info):
    for state in STATES:
        if batches_info[(day,batch,state)].x == 1:
            return state
    raise NotSolvableError