from app.model.bobail.action_space import get_action_index

def test_action_index(game):
	game.move([9, 13])

	for direction, rows in enumerate(get_action_space()):
		for row, columns in enumerate(rows):
			for column, move in enumerate(columns):
				if move is not None:
					assert get_action_index(game, move) == convert_to_index(direction, row, column)

def convert_to_index(direction, row, column):
	return (direction * 8 * 4) + (row * 4) + column

def get_action_space():
	return [
		[
			[None, None, None, None, None],
			[[6, 2], [7, 3], [8, 4], [9, 5], None],
			[[11, 7], [12, 8], [13, 9], [14, 10], None],
			[[16, 12], [17, 13], [18, 14], [19, 15], None],
			[[21, 17], [22, 18], [23, 19], [24, 20], None],
		],
		""" [
			[None, None, None, None],
			[[5, 1], [6, 2], [7, 3], [8, 4]],
			[[9, 6], [10, 7], [11, 8], None],
			[[13, 9], [14, 10], [15, 11], [16, 12]],
			[[17, 14], [18, 15], [19, 16], None],
			[[21, 17], [22, 18], [23, 19], [24, 20]],
			[[25, 22], [26, 23], [27, 24], None],
			[[29, 25], [30, 26], [31, 27], [32, 28]]
		],
		[
			[[1, 5], [2, 6], [3, 7], [4, 8]],
			[None, [6, 9], [7, 10], [8, 11]],
			[[9, 13], [10, 14], [11, 15], [12, 16]],
			[None, [14, 17], [15, 18], [16, 19]],
			[[17, 21], [18, 22], [19, 23], [20, 24]],
			[None, [22, 25], [23, 26], [24, 27]],
			[[25, 29], [26, 30], [27, 31], [28, 32]],
			[None, None, None, None]
		],
		[
			[[1, 6], [2, 7], [3, 8], None],
			[[5, 9], [6, 10], [7, 11], [8, 12]],
			[[9, 14], [10, 15], [11, 16], None],
			[[13, 17], [14, 18], [15, 19], [16, 20]],
			[[17, 22], [18, 23], [19, 24], None],
			[[21, 25], [22, 26], [23, 27], [24, 28]],
			[[25, 30], [26, 31], [27, 32], None],
			[None, None, None, None]
		],
		[
			[None, None, None, None],
			[None, None, None, None],
			[None, [10, 1], [11, 2], [12, 3]],
			[None, [14, 5], [15, 6], [16, 7]],
			[None, [18, 9], [19, 10], [20, 11]],
			[None, [22, 13], [23, 14], [24, 15]],
			[None, [26, 17], [27, 18], [28, 19]],
			[None, [30, 21], [31, 22], [32, 23]]
		],
		[
			[None, None, None, None],
			[None, None, None, None],
			[[9, 2], [10, 3], [11, 4], None],
			[[13, 6], [14, 7], [15, 8], None],
			[[17, 10], [18, 11], [19, 12], None],
			[[21, 14], [22, 15], [23, 16], None],
			[[25, 18], [26, 19], [27, 20], None],
			[[29, 22], [30, 23], [31, 24], None]
		],
		[
			[None, [2, 9], [3, 10], [4, 11]],
			[None, [6, 13], [7, 14], [8, 15]],
			[None, [10, 17], [11, 18], [12, 19]],
			[None, [14, 21], [15, 22], [16, 23]],
			[None, [18, 25], [19, 26], [20, 27]],
			[None, [22, 29], [23, 30], [24, 31]],
			[None, None, None, None],
			[None, None, None, None]
		],
		[
			[[1, 10], [2, 11], [3, 12], None],
			[[5, 14], [6, 15], [7, 16], None],
			[[9, 18], [10, 19], [11, 20], None],
			[[13, 22], [14, 23], [15, 24], None],
			[[17, 26], [18, 27], [19, 28], None],
			[[21, 30], [22, 31], [23, 32], None],
			[None, None, None, None],
			[None, None, None, None]
		] """
	]