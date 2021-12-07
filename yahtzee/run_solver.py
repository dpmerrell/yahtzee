
import pickle as pkl
from yahtzee.solve import solve_game


if __name__=="__main__":

    game_state_values = solve_game()

    pkl.dump(game_state_values, open("game_state_values.pkl", "wb"))

