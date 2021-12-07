

from yahtzee.payoffs import compute_payoff
from yahtzee.dice import dice_to_state, state_to_dice

class InteractiveGame:
    
    def __init__(self, game_state=None, turn_state=None):

        if game_state is None:
            game_state = (False,)*13
        self.game_state = game_state

        if turn_state is None:
            turn_state = (0, None)
        self.turn_state = turn_state

        self.history = []


    def receive_action(self, action):
        roll = self.turn_state[0]

        if isinstance(action, tuple):
            # Validate action (TODO)
            assert roll <= 2
            assert len(action) == 6
            assert sum(action) <= 5

            # Roll the dice
            dice_ls = self.roll_dice(action=action)
            self.turn_state = (roll + 1, dice_to_state(dice_ls))
        else:
            assert isinstance(action, int)


    def roll_dice(self, action=None):

        if action is None:
            action = (5,)

        while True:
            if sum(action) == 5:
                print_str = "\tRoll all of your dice! "
            else:
                rolled_dice = [str(d) for d in state_to_dice(action)]

                print_str = "\tRe-roll the following dice: {}. ".format(", ".join(rolled_dice))

            print_str += "\n\tEnter all of your dice here: "

            dice_str = input(print_str)
            dice_ls = [int(x) for x in dice_str if x.isdigit()]

            # Validate dice (TODO)
            is_valid = (len(dice_ls) == 5 and all([x >= 1 and x <= 6 for x in dice_ls]))
            if is_valid:
                break

            print("Error! '{}' isn't valid input. Let's try this again...".format(dice_str))

        return tuple(dice_ls)


    def start_turn(self):
        self.turn_state = (1, dice_to_state(self.roll_dice()))


    def end_turn(self, action):
        # Update the game history
        dice_state = self.turn_state[1]
        score = compute_payoff(action, dice_state)
        self.history.append((action, score))

        # Update the game state
        self.game_state = self.game_state[:action] \
                          + (True,) \
                          + self.game_state[action+1:]

        # Reset the turn state
        self.turn_state = (0, None)


