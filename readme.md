A Python Flask app that uses unsupervised learning to train a neural network to learn how to play bobail.

This was built to work in conjunction with the [web app](TBD) and can easily be run in a Kubernetes cluster [here](TBD). This app receives requests from the web app to restart the training, predict a move, or analyze previous training sessions. A mysql database is used for organizing the sessions and a cron flask script is used to perform the training runs.

[![Build Status](https://travis-ci.org/ImparaAI/checkers-prediction.png?branch=master)](https://travis-ci.org/ImparaAI/checkers-prediction)

# Routes

## /predict
Method: `GET`

Input: `moves=[[int, int], [int, int], ...]`

Output: `[int, int]`

## /training/session
Method: `POST`

Input: `episodes=int, time_limit_in_seconds=int`

## /training/sessions
Method: `GET`

# Commands

All commands can be run from the app root. If you are running this in the docker container, you don't need to worry about these as they are handled automatically.

## Initialize database

```
flask database:initialize
```

This only needs to be run if the database is not initialized, otherwise nothing will happen. The docker start script runs this on container startup.

## Run the next training session

```
flask training_session:run
```

Runs the next available training session. If a session is currently training, this will do nothing. This is run on a per-minute cron job in the docker container.

# Assumptions

The rules used are those defined by [the bobail library](https://github.com/jasondaming/bobail). Importantly, each piece movement is completely distinct, the bobail is regarded as belonging to a third player so neither player "owns" it, and each move (after the first) consists of a bobail move (1 space) then a regular move (till it runs into something).

# Training strategy

This app uses a [Monte Carlo tree search library](https://github.com/ImparaAI/monte-carlo-tree-search) that roughly follows the methods used by [AlphaGo Zero](https://www.nature.com/articles/nature24270.epdf?author_access_token=VJXbVjaSHxFoctQQ4p2k4tRgN0jAjWel9jnR3ZoTv0PVW4gB86EEpGqTRDtpIz-2rmo8-KG06gqVobU5NSCFeHILHcVFUeMsbvwS-lxjqQGg98faovwjxeTUgZAUMnRQ). In short, every time it's the AI's turn to move, it uses one neural net to reduce the number of moves it should consider and another to evaluate the expected value of any particular move as we traverse the tree of possible moves in future rounds. In Google's terminology these are called the "policy network" and the "value network" respectively.

Each training run starts the neural net over from scratch. By default, a training run lasts for 1000 games, but it's also possible to restrict this on time and number of games depending on the limitations of your machine.

## Neural network architecture

The neural net's job is to reduce the amount of digging for the Monte Carlo tree search algorithm. The network itself is structurally identical to the AlphaZero network with the exception of the inputs, the predicted outputs, and certain small details in the convolutional layers

### Input

The input to the neural net is a multidimensional numpy array that is `43 x 5 x 5` (depth x height x width), or `43` layers of `5 x 5` 2d arrays. The `5 x 5` is determined by the shape of the board. The `43` is made up like this:

- Layers **1-42** hold the state of the board's pieces for the last 14 moves. So layers **1-3** hold the board state for the most recent move, layers **4-6** hold the board state for the second most recent move, etc. Within a single move's board state, the first layer describes the position of the current player's pieces, the second layer is for the current opponent's pieces, and the third is the location of the bobail. The distinction between the current player and the opponent is important as the neural net only ever makes predictions from the perspective of the current player.
- Layer **43** has all 0s if it's player 1's turn and all 1s if it's player 2's turn.

The end result is that every value in this multidimensional input is either a `1` or a `0` and it fully represents everything about the current state of the board and the 13 previous moves.

### Outputs

The neural net has two outputs:

- A float that represents the expected win value for the current player given the current board state. In the Monte Carlo tree search algorithm this is the `W` value for the node being evaluated.
- A flat list 200 elements long, each of which hold a float value between `0` and `1` representing a success probability for choosing that move. Each spot on the board gets 8 potential move positions representing the direction and the distance of the move. So positions `0-7` in this array are reserved for spot 1's potential moves:

- **0**: move to the southwest
- **1**: move to the west
- **2**: move to the northwest
- **3**: move to the south
- **4**: move to the north
- **5**: move to the southeast
- **6**: move to the east
- **7**: move to the northeast

This is repeated for all 25 positions on the board, for a total of 200 elements.

During training, the output values are `0` for all impossible moves and a value between `0` and `1` for all possible moves. The value is determined by the number of visits in the Monte Carlo tree search simulation relative to the other possible moves. When the Monte Carlo tree search is making decisions about which moves to populate as child nodes, it iterates over all possible moves and finds the probability values (`p`) for them from this output, which eliminates the need to drill down further for that child node as you might do in a non-NN MCTS algorithm.

### Differences with AlphaZero

By default, this app uses 75 convolution kernels (i.e. "neurons") per convolutional layer whereas AlphaZero uses 256. AlphaZero also uses 40 residual layers where this app uses 6. The reasons for this are:

- Bobail is inherently simpler than Chess or Go
- We expect training to work decently on a moderately powerful CPU, rather than necessarily on a GPU or TPU

It's worth keeping in mind that in neural nets finding the right number of "neurons" and residual layers is a bit of an art. There may indeed be a way of precisely quantifying the correlation between prediction accuracy and these hyperparameters for specific problems, but when this app was made it was not immediately obvious to us how to do it. Our method for choosing these numbers was a process of trial and error with a goal of minimizing them (for performance) while subjectively keeping a high enough prediction accuracy.

# Why bobail?

It is a relatively simple game that it appears that no one else has done any in depth strategy analysis on. This app's training can be run on a relatively cheap machine and doesn't really require a GPU or TPU.

# Testing

Run `pytest`.

The training tests run a simplified session with only 1 game. The prediction tests use a randomized neural net.