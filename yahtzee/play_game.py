
from game_player import OptimalPlayer
from game import InteractiveGame
from payoffs import PAYOFF_LS
import pickle as pkl


def play_game(player, game, verbose=True):

    if verbose:
        print("\n######## STARTING GAME ########\n")  
 
    # While the game isn't finished...
    turn = 0
    while False in game.game_state:
        turn += 1

        game.start_turn()
        player.set_game_state(game.game_state)
        action = 0
        
        # While the turn isn't finished... 
        while game.game_state[0] < 3:
            player.set_turn_state(game.turn_state)
            action = player.get_action()
            game.receive_action(action)

            if isinstance(action, int):
                print("\nClaim the '{}' reward!\n".format(PAYOFF_LS[action][0]))
                break
        
        game.end_turn(action) 
        if verbose:
            print(make_score_card(game.history))
            print("\n######## FINISHED TURN {} ########\n".format(turn))

    if verbose:
        print("Game is finished!") 
        print(make_score_card(game.history))

    return game_history


def make_score_card(player_history):
    
    scorecard = "Score card:\n"

    score_dict = {payoff_name: "__" for payoff_name, _ in PAYOFF_LS}
    total = 0
    for action, score in player_history:
        score_dict[PAYOFF_LS[action][0]] = score
        total += score

    for payoff_name, _ in PAYOFF_LS:
        scorecard += "\t{}:\t{}\n".format(payoff_name, score_dict[payoff_name])

    scorecard += "\tTOTAL: {}".format(total)

    return scorecard


if __name__=="__main__":

    # Initialize an optimal player
    game_state_values = pkl.load(open("game_state_values.pkl","rb"))
    player = OptimalPlayer(game_state_values)
    
    # Initialize the game
    game = InteractiveGame()

    play_game(player, game)


