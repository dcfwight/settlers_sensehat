from random import choice, sample, shuffle, randint
from sense_hat import SenseHat
import os

sense = SenseHat()

def dice_throw():
	"""return a tuple of two dice randomly"""
	return(randint(1,6), randint(1,6))

def create_full_deck(n):
	"""create n full decks, each with 36 tuples of the dice rolls"""
	deck = []
	for card in range(n):
		for d1 in range (1,7):
			for d2 in range (1,7):
				deck.append((d1,d2))
	return deck

def augment_deck(deck, n_remove=0, n_add=0):
	"""from a deck of cards, shuffle them, remove n_remove cards
	replace with n_return random cards"""
	shuffle(deck) # this shuffles cards in-line

	# can only remove as many cards as there are in the deck
	n_remove = min(len(deck), n_remove)
	# cannot be negative
	n_remove = max(0, n_remove)

	deck = sample(deck, len(deck) - n_remove)

	# Add in n_add random cards - these cannot be negative
	n_add = max(0, n_add)
	for i in range (n_add):
		deck.append(dice_throw())

	return deck

def report(roll, player):
	d1, d2 = roll
	print ('{} rolled {}. {} + {}'.format(player, d1+d2, d1, d2))

def test():
	deck = create_full_deck(2)
	deck = augment_deck(deck, n_remove = 10, n_add=10)
	report(deck.pop(), 'Alice')
	
def main():
	pass

if __name__ == "__main__":
	test()
	main()
