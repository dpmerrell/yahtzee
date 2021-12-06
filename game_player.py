
import dice
import solve

class OptimalPlayer:

    def __init__(self, game_state_values):

        self.game_state_values = game_state_values
        self.current_game_state = tuple([False]*13)
        self.current_turn_state = (0,())
        self.history = []

        policy, values = solve.solve_turn(self.current_game_state,
                                          self.game_state_values)
        self.turn_policy = policy
        self.turn_values = values
 

    def update_dice(dice_list):
        dice_state = dice.dice_to_state(dice_list)
        current_roll = self.current_turn_state[0]
        self.current_turn_state = (current_roll+1, dice_state)


    def get_action():
        roll = self.current_turn_state[0]
        if roll > 0:
            action = self.turn_policy[self.current_turn_state]
        else:
            action = (0,0,0,0,0,0)
        return action


    def get_value():
        roll = self.current_turn_state[0]
        if roll > 0:
            value = self.turn_values[self.current_turn_state]
        else:
            value = self.game_state_values[self.current_game_state]
        return value
        

    def end_turn(action):

        # Update the game history
        dice_state = self.current_turn_state[1]
        score = compute_payoff(dice_state, action)
        self.history.append((action, score))

        # Update the game state
        self.current_game_state = self.current_game_state[:action] \
                                  + (True,) \
                                  + self.current_game_state[action+1:]

        self.turn_policy = solve.solve_turn(self.current_game_state,
                                            self.game_state_values)

        # Reset the turn state
        self.current_turn_state = (0,())


