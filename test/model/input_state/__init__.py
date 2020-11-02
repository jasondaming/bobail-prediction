import numpy as np

def build_initial_state():
	input_state = np.zeros((43, 5, 5), dtype = np.int)

	input_state[0] = [[1, 1, 1, 1, 1],
	                  [0, 0, 0, 0, 0],
	                  [0, 0, 0, 0, 0],
	                  [0, 0, 0, 0, 0],
	                  [0, 0, 0, 0, 0]]

	input_state[1] = [[0, 0, 0, 0, 0],
	                   [0, 0, 0, 0, 0],
	                   [0, 0, 0, 0, 0],
	                   [0, 0, 0, 0, 0],
					   [1, 1, 1, 1, 1]]

	input_state[2] = [[0, 0, 0, 0, 0],
	                   [0, 0, 0, 0, 0],
	                   [0, 0, 1, 0, 0],
	                   [0, 0, 0, 0, 0],
					   [0, 0, 0, 0, 0]]

	return input_state

def play_moves(game, moves):
	boards = [game.board]

	for move in moves:
		game.move(move)
		boards.append(game.board)

	return boards