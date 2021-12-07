"""
iterators.py

Some useful iterators
"""
import itertools as it

def _rec_dice_state_iter(vec):

    if len(vec) == 1:
        yield vec
    else:
        while vec[0] >= 0:
            for suffix in _rec_dice_state_iter(vec[1:]): 
                yield vec[:1] + suffix 
            vec[0] -= 1
            vec[1] += 1

"""
Iterate through unique dice states.
"""
def dice_state_iter(n_dice, n_sides):

    vec = [n_dice] + [0]*(n_sides-1)

    for vec in _rec_dice_state_iter(vec):
        yield tuple(vec)
       

"""
Iterate through the possible "sub-states" of 
a dice state. I.e., the states obtained by
removing dice from a state.
""" 
def dice_substate_iter(dice_state):

    for substate in it.product(*[range(count+1) for count in dice_state]):
        yield substate


"""
Iterate through possible game states -- i.e.,
the possible combinations of filled/empty 
column entries.
"""
def game_state_iter():

    for r in range(14):
        for idx_tuple in it.combinations(range(13), r):
            state = [True]*13
            for idx in idx_tuple:
                state[idx] = False
            yield tuple(state)

"""
Given a game state, iterate through the 
available "payoff" actions
"""
def payoff_action_iter(game_state):

    for idx, box in enumerate(game_state):
        if box == False:
            yield idx



"""
Iterate through the "turn" states 
(i.e., all possible dice states for the three possible rolls) 
"""
def turn_state_iter():
    for roll in range(3, 0, -1):
        for dice_state in dice_state_iter(5,6):
            yield (roll, dice_state)



