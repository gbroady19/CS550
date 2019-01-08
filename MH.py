# I have seen this problem before, so unfourtunatly the surprise is spoiled. However, I do remember orginally thinking that changing your choice should not affect the outcome. 

import random as r

prizecount = 0
for x in range(1000):
	choice = r.randrange(1,4)
	#3 is the winning door 
	if choice == 3:
		prizecount+=1 
print(prizecount)

prizecount2 = 0
for x in range (1000):
	choice = r.randrange(1,4)
	if choice == 1: 
		#host would eliminate door 2 so you would choose 3, thus get the prize 
		prizecount2+=1 
	if choice == 2:
		#host would eliminate door 1 so you would choose 3, thus get the prize 
		prizecount2+=1 
	#The only way you wouldn't get the prize is if you chose 3 to start with



print(prizecount2)

'''
I found the website montyhallproblem.com very useful in understanding this. The thing that made the problem click in my mind is realizing that by always reveiling a door that does not have the prize in it, you are actually given a lot of information. If the host reveiled just a random door then it would be a very different problem. Once a losing door is reveiled, we know that our original door has a 1/3 (which was clear at the start) chance of containing a prize, and the total probablilty must add up to 1, so the other door must have a 2/3 chance. This is reflected well in the data from the simulation and more clear from the way the program is actually written.

'''

