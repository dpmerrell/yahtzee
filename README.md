# yahtzee
A Yahtzee-solving python package and command line tool.

The algorithm yields the mathematically-guaranteed optimal strategy*. That is, it maximizes expected score for a single game of Yahtzee.

The command line tool (`play_yahtzee`) guides you through a game and advises you on the best moves to make.

The algorithm assumes "vanilla" rules. It attains an average score of 229.638 points.

***Important caveat**: the algorithm does not account for the 35-point upper section bonus. In practice it usually gets the bonus. Even when it doesn't, it attains a very high score (the 229.683 average excludes the bonus!). A future version may account for the bonus, but it would significantly increase the size of the state space.

## Installation

Make sure you have python >= 3.8.
I recommend using a virtual environment:

`$ source my_py38_env`

Install the [`yahtzee-solve` project](https://pypi.org/project/yahtzee-solve/) from PyPI, via pip:

```
(my_py38_env)$ pip install yahtzee-solve
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

Just enter your dice as a sequence of five numbers: E.g., `31624` or `63236`.

## Python package
The `yahtzee` python package has the following components:
* A dynamic programming algorithm that solves the whole game (`solve_game`, `solve_turn`)
* Precomputed results for that algorithm (`PRECOMP_STATE_VALUES`) (you can compute those results for yourself, but it will take hours)
* An object-oriented interface for the algorithm to interact with a game of Yahtzee (`OptimalPlayer`, `InteractiveGame`)
* A command line script based on that interface (`play_interactive_game()`)

You would only need to deal with the package if you were incorporating the solver into some larger project.

The source code is small -- look through it for details.

## Algorithmic ideas

Yahtzee is a [Markov Decision Process](https://en.wikipedia.org/wiki/Markov_decision_process).
It has convenient properties that make it straightforward to solve.

The solver uses dynamic programming to compute the best action for every possible state in a game of Yahtzee.
It iterates through every possible state and finds the action yielding maximal expected score (subject to the game's randomness).
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
