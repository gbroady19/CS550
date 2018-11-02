'''
DECK OF CARDS:

Properties: 

Suite - h,d,c,s
rank - 2-10, J,K, Q, K, A 
		1-13 
----------------------

use __Str__ function 


Deck:
List of cards/empty list 
-------------
Draw a card/dealing a card 
Shuffling 
Play a card 

'''

class Card:
	def __init__(self,s,r):
		self.s = s
		self.r = r

	def __str__(self):
		if self.r == 11: 
			rank = "Jack"
		elif self.r == 12: 
			rank = "Queen"
		elif self.r == 13:
			rank = "King"
		elif self.r == 14: 
			rank = "Ace"
		else: 
			rank = str(self.r)

		if self.s == 1:
			suite = "Hearts"
		if self.s == 2:
			suite = "Diamonds"
		if self.s == 3:
			suite = "Clubs"
		if self.s == 4: 
			suite = "Spades" 
		return ""+rank+" of "+suite+""

