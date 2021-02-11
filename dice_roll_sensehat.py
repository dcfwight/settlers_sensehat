from random import choice, sample, shuffle, randint
import os

def dice_throw():
	"""return a tuple of two dice randomly"""
	return(randint(1,6), randint(1,6))

def create_full_deck(n):
	"""create n full decks"""
	deck = []
	for card in range(n):
		for d1 in range (1,7):
			for d2 in range (1,7):
				deck.append((d1,d2))
	return deck

def test():
	pass

def main():
	pass



if __name__ == "__main__":
	test()
	main()
