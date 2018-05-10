import player_logic
import ships
import board_logic



##############################
def main():
	testCarrier = ships.Carrier('A', 1, 'S')
	testDestroyer = ships.Destroyer('B', 3, 'E')
	testCruiser = ships.Cruiser('A', 2, 'E')
	print(testCarrier.location)

	b = board_logic.Board()
	b.addShip(testCarrier)
	b.addShip(testDestroyer)
	b.addShip(testCruiser)
	b.dispBoard()

	m = player_logic.Move(b)

	m.promptMovePlacement()

if __name__ == '__main__':
	main()
