#it is the state of the game at a particular
class game(object):

	# A function to initialize the board at the start of the game
	def __init__(self,init_array,startr,startc,maxr,maxc):

		active_cells = []

		# Finding the active cells
		for r , single_row in enumerate(init_array.splitlines()):
			for c , unit in enumerate(single_row.strip()):
				if unit == 'o':
					active_cells.append((r,c))

		# initializing the board
		board = [[False] * maxc for r in range(maxr)]
		for cell in active_cells:
			board[cell[0] + startr][cell[1] + startc] = True

		self.board = board
		self.maxr = maxr
		self.maxc = maxc

	# A function to display the board
	def display(self):
		output = ''

		for r , single_row in enumerate(self.board):
			for c , unit in enumerate(single_row):
				if self.board[r][c]:
					output += ' o'
				else:
					output += ' .'
			output += '\n'

		return output

glider = """oo.
			o.o
			o.."""

myGame = game(glider,2,3,10,10)