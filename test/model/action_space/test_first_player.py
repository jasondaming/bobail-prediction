from app.model.bobail.action_space import get_action_index

def test_action_index(game):
	for direction, rows in enumerate(get_action_space()):
		for row, columns in enumerate(rows):
			for column, move in enumerate(columns):
				if move is not None:
					assert get_action_index(game, move) == convert_to_index(direction, row, column)

def convert_to_index(direction, row, column):
	return direction + ((row * 5) + column) * 8

def get_action_space():
	return [
		[
			[[2225, 19], [24, 18], [23, 17], [22, 16], None],
			[None, [7, 11], [8, 12], [9, 13], [10, 14]],
			[[11, 7], [12, 8], [13, 9], [14, 10], None],
			[[16, 12], [17, 13], [18, 14], [19, 15], None],
			[[21, 17], [22, 18], [23, 19], [24, 20], None],
		],
		[
			[[25, 24], [24, 23], [23, 22], [22, 21], None],
			[[20, 19], [19, 18], [18, 17], [17, 16], None],
			[[15, 14], [14, 13], [13, 12], [12, 11], None],
			[[10, 9], [9, 8], [8, 7], [7, 6], None],
			[[5, 4], [4, 3], [3, 2], [2, 1], None]
		],
		""" 		[
			[[32, 28], [31, 27], [30, 26], [29, 25]],
			[None, [27, 24], [26, 23], [25, 22]],
			[[24, 20], [23, 19], [22, 18], [21, 17]],
			[None, [19, 16], [18, 15], [17, 14]],
			[[16, 12], [15, 11], [14, 10], [13, 9]],
			[None, [11, 8], [10, 7], [9, 6]],
			[[8, 4], [7, 3], [6, 2], [5, 1]],
			[None, None, None, None]
		],
		[
			[[32, 27], [31, 26], [30, 25], None],
			[[28, 24], [27, 23], [26, 22], [25, 21]],
			[[24, 19], [23, 18], [22, 17], None],
			[[20, 16], [19, 15], [18, 14], [17, 13]],
			[[16, 11], [15, 10], [14, 9], None],
			[[12, 8], [11, 7], [10, 6], [9, 5]],
			[[8, 3], [7, 2], [6, 1], None],
			[None, None, None, None]
		],
		[
			[None, None, None, None],
			[None, None, None, None],
			[None, [23, 32], [22, 31], [21, 30]],
			[None, [19, 28], [18, 27], [17, 26]],
			[None, [15, 24], [14, 23], [13, 22]],
			[None, [11, 20], [10, 19], [9, 18]],
			[None, [7, 16], [6, 15], [5, 14]],
			[None, [3, 12], [2, 11], [1, 10]]
		],
		[
			[None, None, None, None],
			[None, None, None, None],
			[[24, 31], [23, 30], [22, 29], None],
			[[20, 27], [19, 26], [18, 25], None],
			[[16, 23], [15, 22], [14, 21], None],
			[[12, 19], [11, 18], [10, 17], None],
			[[8, 15], [7, 14], [6, 13], None],
			[[4, 11], [3, 10], [2, 9], None]
		],
		[
			[None, [31, 24], [30, 23], [29, 22]],
			[None, [27, 20], [26, 19], [25, 18]],
			[None, [23, 16], [22, 15], [21, 14]],
			[None, [19, 12], [18, 11], [17, 10]],
			[None, [15, 8], [14, 7], [13, 6]],
			[None, [11, 4], [10, 3], [9, 2]],
			[None, None, None, None],
			[None, None, None, None]
		],
		[
			[[32, 23], [31, 22], [30, 21], None],
			[[28, 19], [27, 18], [26, 17], None],
			[[24, 15], [23, 14], [22, 13], None],
			[[20, 11], [19, 10], [18, 9], None],
			[[16, 7], [15, 6], [14, 5], None],
			[[12, 3], [11, 2], [10, 1], None],
			[None, None, None, None],
			[None, None, None, None]
		] """
	]