import numpy as np

NORTH_WEST = 0
WEST = 1
SOUTH_WEST = 2
NORTH = 3
SOUTH = 4
NORTH_EAST = 5
EAST = 6
SOUTH_EAST = 7

def get_action_index(game, move):
	from_row = position_to_row(move[0], game)
	to_row = position_to_row(move[1], game)
	from_column = position_to_column(move[0], game)
	to_column = position_to_column(move[1], game)
	direction = get_direction(from_row, from_column, to_row, to_column, game.whose_turn())
	print(str(from_row) + str(from_column) + str(direction))
	return (((from_row * game.board.width) + from_column) * 8) + direction

def position_to_row(position, game):
	row = (position - 1) // game.board.width
	return translate_row(row, game.board.height, game.whose_turn())

def position_to_column(position, game):
	column = (position - 1) % game.board.width
	return translate_column(column, game.board.width, game.whose_turn())

def get_direction(from_row, from_column, to_row, to_column, player_turn):
	row_direction = to_row - from_row
	column_direction = to_column - from_column

	directions = {
		-1: {
			0: NORTH,
			-1: NORTH_WEST,
			1: NORTH_EAST,
		},
		0: {
			0: None,
			-1: WEST,
			1: EAST,
		},
		1: {
			0: SOUTH,
			-1: SOUTH_WEST,
			1: SOUTH_EAST,
		},
	}

	return directions[row_direction][column_direction]

def translate_row(row, board_height, player_turn):
	return board_height - 1 - row if player_turn == 1 else row

def translate_column(column, board_width, player_turn):
	return board_width - 1 - column if player_turn == 1 else column