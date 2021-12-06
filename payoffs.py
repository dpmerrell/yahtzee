

def compute_payoff(action, dice_state):

    if action == 0:
        return ones_payoff(dice_state)
    if action == 1:
        return twos_payoff(dice_state)
    if action == 2:
        return threes_payoff(dice_state)
    if action == 3:
        return fours_payoff(dice_state)
    if action == 4:
        return fives_payoff(dice_state)
    if action == 5:
        return sixes_payoff(dice_state)
    if action == 6:
        return three_of_a_kind_payoff(dice_state)
    if action == 7:
        return four_of_a_kind_payoff(dice_state)
    if action == 8:
        return full_house_payoff(dice_state)
    if action == 9:
        return small_straight_payoff(dice_state)
    if action == 10:
        return large_straight_payoff(dice_state)
    if action == 11:
        return yahtzee_payoff(dice_state)
    if action == 12:
        return chance_payoff(dice_state)


def ones_payoff(dice_state):
    return dice_state[0]

def twos_payoff(dice_state):
    return 2.0*dice_state[1]
   
def threes_payoff(dice_state):
    return 3.0*dice_state[2]

def fours_payoff(dice_state):
    return 4.0*dice_state[3]

def fives_payoff(dice_state):
    return 5.0*dice_state[4]

def sixes_payoff(dice_state):
    return 6.0*dice_state[5]

def three_of_a_kind_payoff(dice_state):
    if 3 in dice_state or 4 in dice_state or 5 in dice_state:
        return float(sum((i+1)*count for i, count in enumerate(dice_state)))
    else:
        return 0.0

def four_of_a_kind_payoff(dice_state):
    if 4 in dice_state or 5 in dice_state:
        return float(sum((i+1)*count for i, count in enumerate(dice_state)))
    else:
        return 0.0

def full_house_payoff(dice_state):
    if 3 in dice_state and 2 in dice_state:
        return 25.0
    else:
        return 0.0

def small_straight_payoff(dice_state):
    is_valid = False
    straight_count = 0
    for count in dice_state:
        if count > 0:
            straight_count += 1
            if straight_count >= 4:
                is_valid = True
                break
        else:
            straight_count = 0
    if is_valid: 
        return 30.0
    else:
        return 0.0


def large_straight_payoff(dice_state):
    if dice_state == (0,1,1,1,1,1) or dice_state == (1,1,1,1,1,0):
        return 40.0
    else:
        return 0.0


def yahtzee_payoff(dice_state):
    if 5 in dice_state:
        return 50.0
    else:
        return 0.0

def chance_payoff(dice_state):
    return sum((i+1)*count for i, count in enumerate(dice_state))


