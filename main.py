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

# These are some models , you can also include your own
glider = """oo.
			o.o
			o.."""

boat = """oo.
		  o.o
		  .o."""

blinker = """ooo"""

beehive = """.oo.
			 o..o
			 .oo."""

loaf = """.oo.
		  o..o
		  .o.o
		  ..o."""

diehard = """......o.
			 oo......
			 .o...ooo"""

acorn = """.o.....
		   ...o...
		   oo..ooo"""

pentomino = """.oo
			   oo.
			   .o."""

spaceship = """oooo.
			   o...o
			   o....
			   .o..o"""

class interaction_user(object):

	def take_input(self):
		print "Enter the height and width of the game of life."
		answer = raw_input()
		self.maxr = int(answer.split()[0])
		self.maxc = int(answer.split()[1])
		print "Change the inital subset in code if you want to."
		# Change the intial subset from here if you want to
		self.subset = spaceship
		print "Enter the row and col no from which the subset must start (For the subset of cells which matter)."
		answer = raw_input()
		self.r = int(answer.split()[0])
		self.c = int(answer.split()[1])
		print "Enter the no of steps for which the game of life must run."
		self.steps = int(raw_input())
		print "Enter the time (sec) 1 move should take (similar to 1/(frame_rate))"
		self.time = float(raw_input())
		self.start_game()

	def start_game(self):
		myGame = game(init_state(self.subset,self.r,self.c,self.maxr,self.maxc))
		print myGame.display()
		sleep(self.time)
		for x in range(self.steps):
			os.system('clear')
			myGame.move()
			print myGame.display()
			sleep(self.time)

user1 = interaction_user()
user1.take_input()
