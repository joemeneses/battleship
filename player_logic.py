class Player:
	def __init__(self):
		self.shipsActive = None
		self.previousMoves = []
		#TODO: Move class

	def placeShip(self):
		print("Where do you want to place")
class Move:
	def __init__(self, board):
		self.moveParse = None
		self.move = {}
		self.board = board
	def promptMovePlacement(self):
		while True:
			self.moveParse = input("Player [" + str(self.board.player) + "] What is your next move (ex: a 2)?\n> ")
			digitAppend = ''
			if self.moveParse == 'exit':
				print('--exiting game--')
				return
			for char in self.moveParse:
				if char.isalpha():
					self.move['row'] = char.upper()
				elif char.isdigit():
					digitAppend += char
			self.move['col'] = digitAppend
			if self.validateMove():
				#execute move
				print('VALID MOVE')
			else:
				print("not a valid move. try again.")
			
	def validateMove(self):
		rows = self.board.boardRows()
		cols = self.board.boardCols()
		#print(rows)
		if self.move['row'] not in rows or self.move['col'] not in cols:
			return False
		return True
	#def executeMove(self):
