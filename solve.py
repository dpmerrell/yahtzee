

import iterators as it
from math import inf
from payoffs import compute_payoff
from dice import add_dice_states, dice_state_probability


def remaining_dice(dice_state, n_dice):
    return n_dice - sum(dice_state)


def solve_turn(game_state, game_state_values):

    turn_actions = {}
    turn_values = {}

    # Loop over states
    for u in it.turn_state_iter():

        #print("\t", u)
        u_roll = u[0]
        u_dice = u[1]

        # Loop over actions
        best_value = -inf
        best_action = None

        # "roll" actions
        v_roll = u_roll+1
        if u_roll < 3: # (only consider these if we haven't already rolled three times.)
            for substate in it.dice_substate_iter(u_dice):
                #print("\t\t", substate)
                value = 0.0
                # Loop over possible outcomes
                for new_roll in it.dice_state_iter(remaining_dice(substate, 5), 6):
                    v_dice = add_dice_states(substate, new_roll)
                    p = dice_state_probability(new_roll)
                    value += p * turn_values[(v_roll, v_dice)]
                if value > best_value:
                    best_value = value
                    best_action = action

        # "payoff" actions
        for action in it.payoff_action_iter(game_state):

            # outcome is deterministic for these actions
            next_game_state = game_state[:action] + (True,) + game_state[action+1:]
            value = compute_payoff(action, u_dice) + game_state_values[next_game_state]
            if game_state[10] == False and u_dice == (1,1,1,1,1):
                print("LONG STRAIGHT", action)
                print("\tNEXT GAME STATE", next_game_state)
                print("\tPAYOFF", compute_payoff(action, u_dice))
                print("\tNEXT STATE VALUE", game_state_values[next_game_state])

            if value > best_value:
                best_value = value
                best_action = action

        turn_actions[u] = best_action
        turn_values[u] = best_value
             
    return turn_actions, turn_values



def solve_game():

    game_state_values = {}

    for i, game_state in enumerate(it.game_state_iter()):

        # Handle the case where all boxes have been filled
        if i == 0:
            game_state_values[game_state] = 0.0
            print(i, game_state, "{}".format(game_state_values[game_state]))
            continue

        turn_actions, turn_values = solve_turn(game_state, game_state_values)   
    
        # Expected value for this turn
        game_state_value = 0.0
        for first_state in it.dice_state_iter(5,6):
            game_state_value += dice_state_probability(first_state)*turn_values[(1,first_state)]
        
        game_state_values[game_state] = game_state_value
        
        print(i, game_state, "{}".format(game_state_value))

    return game_state_values


