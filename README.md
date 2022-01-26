# SenseHat Catan dice roller
## Settlers of Catan dice roller using Python SenseHat

### Background
[Settlers of Catan](https://www.catan.com/) is a popular strategy board game  
[SenseHat](https://projects.raspberrypi.org/en/projects/getting-started-with-the-sense-hat) is a RaspberryPi module with lots of sensors - e.g. it can detect shaking, useful for this particular project. 

### Motivation
* The average game of Catan involves 80 dice rolls.
* Ths project evens out the element of chance by simulating using a deck of cards with the 
dice rolls instead of actual dice.
* If the average game is 80 dice rolls, then this is equivalent to
just more than 2 'decks' of dice rolls, each deck consisting of
the 36 potential dice rolls you can get.


The project uses the Sense Hat as input for next turn, reporting and some animation.

## Implementation
1. You will need a RaspberryPi with SenseHat attached.
1. For SenseHat implementation and other RaspberryPi setup guidance, link [here](https://projects.raspberrypi.org/en/projects/getting-started-with-the-sense-hat/0)
1. SSH into RaspberryPi and clone this repository.
1. Move into the cloned directory and enter `python dice_roll.py`
2. The program will then guide you through the setup or run a default deck of dice rolls

### Notes
* There will always be a balance between randomness of dice-rolls and card-counting.
* This program allows you to customise this 
  * The more 'decks' you have, the more random it will be
  * It allows you to increase the randomness by randomly replacing cards after the decks have been chosen. 
