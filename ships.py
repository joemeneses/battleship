class Ship:
	def __init__(self, MAX_HEALTH, name, y, x, direc, desig):
		self.MAX_HEALTH = MAX_HEALTH
		self.name = name
		self.direc = direc #N, S, E, W - from coordinate
		self.x = x
		self.y = y
		self.desig = desig
	
	@property
	def location(self):
		return self.y, self.x
	
	@property
	def direction(self):
		return self.direc
	
	@property
	def designation(self):
		return self.desig
	
	def convertLetterToArrayIndex(self, letter):
		return {
			'A' : 0,
			'B' : 1,
			'C' : 2,
			'D' : 3,
			'E' : 4,
			'F' : 5,
			'G' : 6,
			'H' : 7,
			'I' : 8,
			'J' : 9
		}.get(letter, -1)
	
	def convertNumberToArrayindex(self, num):
		return num - 1

class Carrier(Ship):
	def __init__(self, y, x, direc):
		#print(self.convertLetterToArrayIndex(y))
		Ship.__init__(self, 5, "Carrier", self.convertLetterToArrayIndex(y), self.convertNumberToArrayindex(x), direc, 'A')

class Battleship(Ship):
	def __init__(self, y, x, direc):
		Ship.__init__(self, 4, "Battleship", self.convertLetterToArrayIndex(y), self.convertNumberToArrayindex(x), direc, 'B')

class Cruiser(Ship):
	def __init__(self, y, x, direc):
		print(self.convertLetterToArrayIndex(y))
		print(self.convertNumberToArrayindex(x))
		Ship.__init__(self, 3, "Cruiser", self.convertLetterToArrayIndex(y), self.convertNumberToArrayindex(x), direc, 'C')

class Submarine(Ship):
	def __init__(self, y, x, direc):
		Ship.__init__(self, 3, "Submarine", self.convertLetterToArrayIndex(y), self.convertNumberToArrayindex(x), direc, 'S')

class Destroyer(Ship):
	def __init__(self, y, x, direc):
		Ship.__init__(self, 2, "Destroyer", self.convertLetterToArrayIndex(y), self.convertNumberToArrayindex(x), direc, 'D')
