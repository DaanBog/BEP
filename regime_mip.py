from gurobipy import Model, GRB
import gurobipy as gp
from helper import get_max_fertillizer, get_max_irrigation, next_day, get_first_day, get_day_numeric, get_last_day, get_previous_day
from parameters import *

def call_model():
    mip = Model(name = "Vertical farm schedule")

    # Definition of variables
    # allocations
    tanks = mip.addVars(DAYS, RACKS, lb=0, ub=get_max_fertillizer(BATCHES), vtype = GRB.INTEGER, name='tank')
    irrigation = mip.addVars(DAYS, RACKS, LAYERS, [0,1], lb=0, ub=get_max_irrigation(BATCHES), vtype = GRB.INTEGER, name='irrigation' )
    
    # batches
    batches_keys = BATCHES.keys()
    batches_states = mip.addVars(DAYS,batches_keys,STATES, vtype = GRB.BINARY, name='batch is state on day')

    # Definition of constraints
    
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



    # Definition of objective function
    obj_fn = gp.quicksum(tanks) + gp.quicksum(irrigation) - gp.quicksum([batches_states[(get_last_day(),batch,'h')]])

    mip.setObjective(obj_fn, GRB.MINIMIZE)

    # Call solver
    mip.optimize() 

    for v in mip.getVars():
        if v.x != 0:
            print ('%s: %g' % (v.varName, v.x))

