from random import choice, sample, shuffle, randint
from sense_hat import SenseHat
from time import sleep
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
	while True:
		if sense.stick.get_events():
			break
		sense.show_letter('A')
		sleep(0.2)
		sense.show_letter('7')
		sleep(0.4)
	print ('{} rolled {}. {} + {}'.format(player, d1+d2, d1, d2))
	sense.clear()

##############################################################
# here we have a load of strings for showing numbers and dice #

r = (255,0,0) # red
g = (0,255,0) # green
b = (0,0,255) # bluee
n = (0,0,0)

numbers = {
	2: [
	n,n,n,b,b,n,n,n,
	n,n,b,n,b,n,n,n,
	n,n,n,b,n,n,n,n,
	n,n,b,n,n,n,n,n,
	n,n,b,b,b,b,n,n
	],
	3: [
	n,n,b,b,b,b,n,n,
	n,n,n,n,n,b,n,n,
	n,n,n,b,b,b,n,n,
	n,n,n,n,n,b,n,n,
	n,n,b,b,b,b,n,n
	],
	4: [
	n,n,n,n,b,n,n,n,
	n,n,n,b,b,n,n,n,
	n,n,b,n,b,n,n,n,
	n,b,b,b,b,b,n,n,
	n,n,n,n,b,n,n,n
	],
	5: [
	n,n,n,b,b,b,n,n,
	n,n,n,b,n,n,n,n,
	n,n,n,b,b,b,n,n,
	n,n,n,n,n,b,n,n,
	n,n,n,b,b,b,n,n
	],
	6: [
	n,n,n,n,b,b,n,n,
	n,n,n,b,n,n,n,n,
	n,n,n,b,b,b,n,n,
	n,n,n,b,n,b,n,n,
	n,n,n,b,b,b,n,n
	],
	7: [
	n,n,b,b,b,b,n,n,
	n,n,n,n,n,b,n,n,
	n,n,n,n,b,n,n,n,
	n,n,n,b,n,n,n,n,
	n,n,b,n,n,n,n,n
	],
	8: [
	n,n,n,b,b,b,n,n,
	n,n,n,b,n,b,n,n,
	n,n,n,b,b,b,n,n,
	n,n,n,b,n,b,n,n,
	n,n,n,b,b,b,n,n
	],
	9: [
	n,n,n,b,b,b,n,n,
	n,n,n,b,n,b,n,n,
	n,n,n,b,b,b,n,n,
	n,n,n,n,n,b,n,n,
	n,n,n,n,n,b,n,n
	],
	10: [
	n,n,b,n,b,b,b,n,
	n,b,b,n,b,n,b,n,
	n,n,b,n,b,n,b,n,
	n,n,b,n,b,n,b,n,
	n,n,b,n,b,b,b,n
	],
	11: [
	n,n,b,n,n,b,n,n,
	n,b,b,n,b,b,n,n,
	n,n,b,n,n,b,n,n,
	n,n,b,n,n,b,n,n,
	n,n,b,n,n,b,n,n
	],
	12: [
	n,n,b,n,n,b,b,n,
	n,b,b,n,b,n,n,b,
	n,n,b,n,n,n,b,n,
	n,n,b,n,n,b,n,n,
	n,n,b,n,b,b,b,b
	]
}

dice_face = {
	1: [n,n,n,n,b,n,n,n,n],
	2: [n,b,n,n,n,n,n,b,n],
	3: [n,n,b,n,b,n,b,n,n],
	4: [b,n,b,n,n,n,b,n,b],
	5: [b,n,b,n,b,n,b,n,b],
	6: [b,n,b,b,n,b,b,n,b]
}

def construct_dice_display(d1,d2):
	"""Creates the bottom half of the sense hat display showing dice"""
	display = []
	display+=numbers[d1+d2]
	display+=dice_face[d1][:3]
	display+=[n,n]
	display+=dice_face[d2][:3]
	display+=dice_face[d1][3:6]
	display+=[n,n]
	display+=dice_face[d2][3:6]
	display+=dice_face[d1][6:9]
	display+=[n,n]
	display+=dice_face[d2][6:9]
	return display

def test():
	for i in range(1,7):
		for j in range(1,7):
			display = construct_dice_display(i, j)
			sense.set_pixels(display)
			sleep(1)
	sense.clear()
	deck = create_full_deck(2)
	deck = augment_deck(deck, n_remove = 10, n_add=10)
	#report(deck.pop(), 'Alice')
	
def main():
	pass

if __name__ == "__main__":
	test()
	main()
