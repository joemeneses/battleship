class Board():
	def __init__(self):
		self.size_x = 10
		self.size_y = 10
		self.label_yaxis = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
		self.label_xaxis = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
		self.board = []

		self.initBoard()
		self.playerTurn = 1
	@property
	def player(self):
		return self.playerTurn
	def boardRows(self):
		return self.label_yaxis

	def boardCols(self):
		return self.label_xaxis

	def initBoard(self):
		for x in range(self.size_x):
			self.board.append([])
			#print(x, end='')
			for y in range(self.size_y):
				#print(y)
				self.board[x].append(' ')
		#print(self.board)

	def dispBoard(self):
		print('X', end='')
		labelFlag = 0
		
		#print x axis labels
		for label in self.label_xaxis:
			print (' ' + label, end='')
		
		print('\r')
		#print each row, start with the y axis label
		for y in range(self.size_y):
			for x in range(self.size_x):
				if(labelFlag < 1):
					print(self.label_yaxis[y], end='')
					labelFlag = 1
				print(' ' + self.board[y][x], end='')
			#new line
			print('\r')
			labelFlag = 0
	
	def addShip(self, ship):
		#DEBUG just add a carrier
		#switches will control the direction of populating the ship to the board
		ySwitch = 0
		xSwitch = 0
		print("loc:: " + str(ship.location))
		(ySwitch, xSwitch) = {
			'N': (-1, 0),
			'S': (1, 0),
			'E': (0, 1),
			'W': (0, -1)
		}.get(ship.direction, (0,0))
		
		#print("received:: " + str(xSwitch) + ", " + str(ySwitch))
		#print(self.validateShipPlacement(ship))
		print (str(ySwitch) + ", " + str(xSwitch))
		#check if it's a valid placement before putting the ship on the board
		if(self.validateShipPlacement(ship)):
			for step in range(ship.MAX_HEALTH):
				self.board[ship.location[0] + ySwitch * step][ship.location[1] + xSwitch * step] = ship.designation
		else:
			print("error: unable to place " + ship.name + " in this position/orientation")

	def validateShipPlacement(self, ship):
		ySwitch = 0
		xSwitch = 0
		#print("loc:: " + str(ship.location))
		(ySwitch, xSwitch) = {
			'N': (-1, 0),
			'S': (1, 0),
			'E': (0, 1),
			'W': (0, -1)
		}.get(ship.direction, (0,0))
		for step in range(ship.MAX_HEALTH):
			#first verify it is in bounds
			if (ship.location[0] + ySwitch * step < 0 or ship.location[1] + xSwitch * step < 0 or 
				ship.location[0] + ySwitch * step > self.size_y or ship.location[1] + xSwitch * step > self.size_x):
				return False

			#then verify that the placement doesn't interfere with other ships
			if (self.board[ship.location[0] + ySwitch * step][ship.location[1] + xSwitch * step] != ' '):
				print("char here:: " + self.board[ship.location[0] + ySwitch * step][ship.location[1] + xSwitch * step])
				return False
		#if everything is good, return true
		return True
	

class GameState(Board):
	def __init__(self):
		Board.__init__(self)
		self.boardstate = Board.initBoard()
	