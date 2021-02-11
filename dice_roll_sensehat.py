from random import choice, sample, shuffle
import os

def create_full_deck(n):
	"""create n full decks"""
	deck = []
	for card in range(n):
		for d1 in range (1,7):
			for d2 in range (1,7):
				deck.append((d1,d2))
	return deck

def main():
	deck = create_full_deck(1)
	print (deck)

if __name__ == "__main__":
	main()
