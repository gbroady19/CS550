
#https://stackoverflow.com/questions/41276067/importing-class-from-another-file
import sys
from cards import Card 

class Deck: 
	def __init__(self,f):
		self.f = f 

	def __str__(self):