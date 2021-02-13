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

def report(roll, initial):
	d1, d2 = roll
	while True:
		sense.show_letter(initial)
		if sense.stick.get_events():
			break
		sleep(0.2)
		sense.set_pixels(d1, d2)
		if sense.stick.get_events():
			break
		sleep(0.4)
	sense.clear()

##############################################################
# here we have a load of strings for showing numbers and dice #

r = (140,0,0) # red
g = (0,200,0) # green
b = (0,0,140) # blue
n = (0,0,0) # blank
w = (100,100,100) # dim white

numbers = {
	2: [
	n,n,n,b,b,n,n,n,
	n,n,b,n,n,b,n,n,
	n,n,n,n,b,n,n,n,
	n,n,n,b,n,n,n,n,
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
	n,n,r,r,r,r,n,n,
	n,n,n,n,n,r,n,n,
	n,n,n,n,r,n,n,n,
	n,n,n,r,n,n,n,n,
	n,n,r,n,n,n,n,n
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
	1: [w,w,w,w,g,w,w,w,w],
	2: [w,g,w,w,w,w,w,g,w],
	3: [w,w,g,w,g,w,g,w,w],
	4: [g,w,g,w,w,w,g,w,g],
	5: [g,w,g,w,g,w,g,w,g],
	6: [g,w,g,g,w,g,g,w,g]
}

def construct_dice_display(d1,d2):
	"""Creates the sense hat display showing dice score and individual faces"""
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

####################################################################


def process_player(i, players_dict, player_order, initials):
	player_name = input("Name of player: {}? ".format(i+1))
	player_order.append(player_name)
	player_initial = player_name[0].upper()
	while player_initial in initials:
		print("Sorry, but your initial is already taken")
		player_initial = input('What initial will you use instead? ')
	players_dict[player_name]=player_initial.upper()
	initials.add(player_initial.upper())
	return players_dict, player_order, initials

def test():
	pass

def setup():
	print ("*-"*12 + "*")
	print("Welcome to Settlers Fair Dice Engine!")
	print ("*-"*12 + "*")

	# set up the objects to hold player details
	players_dict={}
	player_order=[]
	initials = set()
	
	n_players = int(input("How many players in the game? "))
	print('OK, please enter them in the order you want to play')
	for i in range(n_players):
		players_dict, player_order, initials = process_player(i,
			players_dict, player_order, initials)
	print ('The players are:')
	print (player_order)
	
	print('Do you wish default deck (36 cards, 4 replaced with random ones)?')
	custom_setup =''
	while custom_setup.upper() not in ['Y','N']:
		custom_setup = input('y for default, n to customise: ')
	
	if custom_setup.upper() == 'Y':
		print('default setup chosen')
		deck = create_full_deck(1)
		deck = augment_deck(deck, n_remove=4, n_add=4)
	
	elif custom_setup.upper() == 'N':
		print ('custom setup chosen')
		n_decks = int(input('How many decks of 36 cards do you want? '))
		deck = create_full_deck(n_decks)
		
		n_remove = int(input('How many cards to remove? '))
		n_add = int(input ('How many random cards to add? '))
		deck = augment_deck(deck, n_remove = n_remove, n_add = n_add)
		
	else:
		print ('we have a problem - not sure what chosen')

	return players_dict, player_order, deck

def turn(counter, player_order, players_dict, deck):
	(d1,d2) = deck.pop()
	print ('Turn: {}'.format(counter+1)) # NB probably want to turn this off to avoid card-counting
	print ("{} threw the dice".format(player_order[counter % len(player_order)]))
	print ('{} thrown, {} and {}'.format(d1+d2, d1, d2))
	report ((d1,d2), players_dict[player])
	return (d1, d2), deck
		   

def main():
	players_dict, player_order, deck = setup()
	counter =0
	print ('{} is first to go'.format(player_order[0]))
	print("Press the SenseHat joystick when ready to roll the dice")
	event = sense.stick.wait_for_event(emptybuffer=True)
	
	while True:
		(d1, d2), deck = turn(counter, player_order, players_dict, deck)
		counter +=1
		# sleep(1) # add in to prevent multiple accidental presses of the joystick
	

if __name__ == "__main__":
	test()
	main()
