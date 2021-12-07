"""
dice.py

Code related to the representation of (fair) dice
and their probabilities.
"""


from math import factorial, prod

DICE_PROB_CACHE = {}



"""
Helper function. Convert a tuple of 
dice values to a dice state tuple.
"""
def dice_to_state(dice_list):
    
    counts = [0]*6
    for die in dice_list:
        counts[die-1] += 1

    return tuple(counts) 


"""
Convert a dice state tuple into a 
tuple of dice. 
"""
def state_to_dice(state_tuple):

    dice = ()
    for i, count in enumerate(state_tuple):
        dice += ((i+1,)*count)
    
    return dice



def _dice_state_probability(state_tuple):

    n_dice = sum(state_tuple)
    denom = prod(factorial(comp) for comp in state_tuple)

    return factorial(n_dice) / denom / (len(state_tuple)**n_dice) 


"""
Compute (and cache) the probability of rolling 
a given set of dice.
"""
def dice_state_probability(state_vec):

    state_tuple = tuple(state_vec)
    p = DICE_PROB_CACHE.get(state_tuple)
    if p is None:
        p = _dice_state_probability(state_tuple)

    return p


"""
Return the sum of two states.
"""
def add_dice_states(state_a, state_b):

    return tuple(a + state_b[i] for i, a in enumerate(state_a))


"""
Return the difference of two states.
"""
def subtract_dice_states(state_a, state_b):
    return tuple(a - state_b[i] for i, a in enumerate(state_a))


