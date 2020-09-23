import numpy as np

def build(game, recent_boards = None):
	return InputBuilder(game, recent_boards).build()

class InputBuilder:

	def __init__(self, game, recent_boards):
		self.game = game
		self.recent_boards = recent_boards[-14:]
		self.player_turn = game.whose_turn()
		self.input = np.zeros((43, self.game.board.height, self.game.board.width), dtype = np.int)

	def build(self):
		for board_index, board in enumerate(reversed(self.recent_boards)):
			board_planes = self.build_board_planes(board)

			self.input[board_index] = board_planes[0]
			self.input[board_index + 6] = board_planes[1]
			self.input[board_index + 12] = board_planes[2]
			self.input[board_index + 18] = board_planes[3]
			self.input[board_index + 24] = board_planes[4]
			self.input[board_index + 30] = board_planes[5]
			self.input[board_index + 36] = board_planes[6]

		self.input[43] = self.build_player_turn(self.game.board)

		return self.input

	def build_board_planes(self, board):
		board_planes = np.zeros((3, board.height, board.width), dtype = np.int)

		for row in range(board.height):
			translated_row = self.translate_row(row, board.height)

			for column in range(board.width):
				translated_column = self.translate_column(column, board.width)
				position = board.position_layout[row][column]
				piece = board.searcher.get_piece_by_position(position)

				if piece:
					if self.player_turn == piece.player:
						plane = 0
					elif self.player_turn == 3:
						plane = 2
					else:
						plane = 1
					board_planes[plane][translated_row][translated_column] = 1

		return board_planes

	def build_player_turn(self, board):
		if self.player_turn == 1:
			return np.zeros((board.height, board.width), dtype = np.int)

		return np.ones((board.height, board.width), dtype = np.int)

	def convert_to_binary_array(self, int_value, array_length):
		binary = "{0:b}".format(int_value).zfill(array_length)
		string_array = list(binary)

		return list(map(int, string_array))

	def translate_row(self, row, board_height):
		return board_height - 1 - row if self.player_turn == 1 else row

	def translate_column(self, column, board_width):
		return board_width - 1 - column if self.player_turn == 1 else column