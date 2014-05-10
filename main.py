import os
from time import sleep

# it is the state of the game at a particular
class init_state(object):

	# A function to initialize the board for the first time
	def __init__(self,init_array,startr,startc,maxr,maxc):

		active_cells = []

		# Finding the active cells
		for r , single_row in enumerate(init_array.splitlines()):
			for c , unit in enumerate(single_row.strip()):
				if unit == 'o':
					active_cells.append((r,c))

		# initializing the board for the next state
		board = [[False] * maxc for r in range(maxr)]
		for cell in active_cells:
			board[cell[0] + startr][cell[1] + startc] = True

		self.board = board
		self.maxr = maxr
		self.maxc = maxc

	# A function to display the board
	def display_state(self):
		output = ''

		for r , single_row in enumerate(self.board):
			for c , unit in enumerate(single_row):
				if self.board[r][c]:
					output += ' o'
				else:
					output += ' .'
			output += '\n'

		return output

# A class containing all the functions that help a game move ahead
class game(object):

	# Initialization of variables
	def __init__(self,state):
		self.state = state
		self.maxr = state.maxr
		self.maxc = state.maxc

	# Function to make life move one step ahead
	def move(self,count=1):

		new_board = [[False] * self.maxc for r in range(self.maxr)]

		for r , single_row in enumerate(self.state.board):
			for c , unit in enumerate(single_row):
				new_board[r][c] = self.find_val(r,c)

		self.state.board = new_board

	# Function to find wether the new cell at the position will be an alive or dead cell
	def find_val(self,r,c):
		alive_count = 0
		for r1 in [-1,0,1]:
			for c1 in [-1,0,1]:
				# Since the board is infinite so we dont need any boundary condition
				alive_count += self.state.board[(r+r1)%self.maxr][(c+c1)%self.maxc]
				if r1==0 and c1==0 and self.state.board[r][c]:
					alive_count -= 1
		if alive_count == 3:
			return True
		if self.state.board[r][c] and alive_count == 2:
			return True
		return False

	def display(self):
		return self.state.display_state()

glider = """oo.
			o.o
			o.."""

myGame = game(init_state(glider,3,4,20,20))
print myGame.display()
sleep(0.45)
for x in range(27):
	os.system('clear')
	myGame.move()
	print myGame.display()
	sleep(0.45)