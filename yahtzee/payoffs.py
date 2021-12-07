

def compute_payoff(action, dice_state):
    return PAYOFF_LS[action][1](dice_state)

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


PAYOFF_LS = [("ones", ones_payoff),
             ("twos", twos_payoff),
             ("threes", threes_payoff),
             ("fours", fours_payoff),
             ("fives", fives_payoff),
             ("sixes", sixes_payoff),
             ("three of a kind", three_of_a_kind_payoff),
             ("four of a kind", four_of_a_kind_payoff),
             ("full house", full_house_payoff),
             ("small straight", small_straight_payoff),
             ("large straight", large_straight_payoff),
             ("Yahtzee", yahtzee_payoff),
             ("chance", chance_payoff)
            ]


