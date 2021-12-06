
import pickle as pkl
import solve


if __name__=="__main__":

    game_state_values = solve.solve_game()

    pkl.dump(game_state_values, open("game_state_values.pkl", "wb"))

