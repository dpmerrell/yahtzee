# yahtzee
A Yahtzee-solving python package and command line tool.

The algorithm is mathematically guaranteed to have the best strategy. That is, it maximizes expected score for a single game of Yahtzee.

The command line tool (`play_yahtzee`) guides you through a game and advises you on the best moves to make.

The algorithm assumes "vanilla" rules. It attains an average score of ~230 points.

## Installation

Clone the repository:

`$ git clone git@github.com:dpmerrell/yahtzee.git`

Make sure you have python >= 3.8.
I recommend using a virtual environment:

`$ source my_py38_env`

Install via pip:

```
(my_py38_env)$ cd yahtzee
(my_py38_env)$ pip install .
```

Congratulations! The `yahtzee` package and `play_yahtzee` command line tool are now installed.

## Command line tool
After installation, you can run the interactive command line tool `play_yahtzee`:

```
(my_py38_env)$ play_yahtzee

###### STARTING GAME ######

    Roll all of your dice!
    Enter all of your dice here:
    
```
The prompts will lead you through a game of Yahtzee and advise you on the best moves to make.

## Python package
The `yahtzee` python package has the following components:
* A dynamic programming algorithm that solves the whole game (`solve_game`, `solve_turn`)
* Precomputed results for that algorithm (`PRECOMP_STATE_VALUES`) (you can compute those results for yourself, but it will take hours)
* An object-oriented interface for the algorithm to interact with a game of Yahtzee (`OptimalPlayer`, `InteractiveGame`)
* A command line script based on that interface (`play_interactive_game()`)

The source code is small -- look through it for details.

## Algorithmic ideas

Yahtzee is a [Markov Decision Process](https://en.wikipedia.org/wiki/Markov_decision_process).
It has convenient properties that make it straightforward to solve.

The solver uses dynamic programming to iterate through every possible state and action in a game of Yahtzee.
For each state, the algorithm computes the maximal expected score (subject to the game's randomness), and the corresponding action.
The algorithm stores these expected scores and optimal actions in a pair of tables.
The table of actions is called the _policy_.

It turns out Yahtzee's state space has an interesting structure that makes it economical to 
1. Store a cache of expected scores for a very small number (2^13 = 8192) of states.
2. At play time, recompute a small portion of the entire game's policy at the beginning of each turn.

This design strikes a balance between memory and computation. A very small number of expected values are stored, but some computation is required during the game.

(In a fully automated setting where speed matters, it may be better to just store the entire policy.)


## Legal stuff

This software is distributed under an MIT license, see LICENSE.txt.

The name "Yahtzee" may or may not be trademarked. I don't know, Hasbro can get in touch with me if they have problems with what I'm doing
