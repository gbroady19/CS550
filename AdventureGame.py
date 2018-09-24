# Adventure Game by KB 
# Based on "Chose your own adventure books." The general theme is based on getting lost on a ski trip and discovering a YETI!! 
# Created 9/23/18 
# Sources for use of time.time : https://www.tutorialspoint.com/python3/time_time.htm
# On my honor, I have neither given nor received unauthrized aid. - KB 

import random
import time

#Begin storyline iniital storyline: 
def start():
	result = input("\n\n Welcome to Adventure game: SKI TRIP GONE WRONG. Please read all text to get full enjoyment from the storyline. \n\nIt all started with a simple ski trip, how could it have gone so wrong? \n\nYou've been lost for a few hours now, trying to get back to the trail. It's getting dark. You see a cave where you can camp for the night, but your gut tells you the trail is right over the next hill. Your next decision might determine your fate \n\n1) Go into the cave for the night. \n2) Keep looking for the trail.\n\n>> ")
	if result == '1':
		cave()
	elif result == '2':
		death1()

	else:
		print("I don't know what "+result+" means. Please type a 1 or a 2. Or press control C to quit.")
		start()
	
def death1(): 
	restart1 = input("You follow your instinct and continue searching for the trail home. It gets darker and darker, colder and colder. You don't survive the night. Press 1 to restart. \n>>")
	if restart1 == '1': 
		start() 
	else: 
		print("I don't know what "+restart1+" means. Please type a 1")
		death1() 

def cave():
	result2 = input("You find some dry branches and start a small fire. Its not enough to keep you warm, but it is enough to keep you alive. The next morning you wake up parched. The snow looks so tempting to eat just as it is.\n\n1) Put snow directly in your mouth.\n2) Rekindle the fire and melt the snow before drinking. \n\n>>")
	
	if result2 == '2':
		food1() 
	elif result2 == '1':
		death2() 
	else: 
		print("I don't know what "+result2+" means. Please type a 1 or a 2")
		cave() 

def death2():
	restart2 = input("You eat what seems like bucket fulls of snow, but the thirstiness never seems to go away. You lay down in the snow and relax. You decide to rest your eyes for a few minutes... which turns into forever \nEnter 1 to restart. \n\n>>")

	if restart2 == '1':  
		start()
	else:  
		print("I don't know what "+restart2+" means. Please type a 1")
		death2() 

def food1(): 
	result3 =input("You drink the water and feel refreshed enough to go search for some food. You see two sets of tracks going in two different directions. One set is small with two toes visible. The other is larger, with four toes. You have a small calibar hunting rifle that your friend suggested you bring along as your only weapon/ Do you follow the large animal for a bigger meal or the smaller one for easier prey \n\n1) Follow the larger tracks. \n2) Follow the smaller tracks. \n\n>>")
	
	if result3 == '1':
		death3() 
	elif result3 == '2':
		result4()

def death3(): 
	restart3 = input("You follow the tracks until you see something large rushing towards you. You fire your weapon but it does nothing. You're no match for the bear. Enter 1 to restart. \n\n>>")
	if restart3 == '1':
		start() 
	else:
		print("I don't know what "+restart3+" means. Please type a 1")
		death3() 

def result4(): 
	result4 = input("You follow the tracks and find a deer waiting. You draw your weapon and do what you have to. You bring it back to the cave and eat some of it, while buring the rest in the snow. You sleep. When you wake up you see some tracks outside leading from the scaps of food you left out. They're different than any you've ever seen. They almost look human but bigger. \n\n1) Follow the tracks \n2) Wait another night for help to come \n\n>>")
	if result4 == '2':
	   death4()
	elif result4 == '1': 
		result5() 
	else: 
		print("I don't know what "+result4+" means. Please type a 1 or a 2")

def death4(): 
	restart4 =input("The creature who's tracks you saw comes back the next night...this time you're the meal. Enter a 1 to restart \n\n>>")
	if restart4 == '1':
		start() 
	else:
		print("I don't know what "+restart4+" means. Please type a 1")
		death4() 

def result5(): 
	result6 = input("The path leads you to a clearing. You see signs of civilization but it still feels unfamilar to you. That's when you see the first one, a Yeti! It's obvious that they see you too. You're faced with a few choices.\n\n1) Fight them. \n2) Attempt to bargain with and befriend them. \n3) Run! \n\n>>") 

	if result6 == '1':
 		end3() 
	elif result6 == '2':
		end2() 
	elif result6 == '3': 
		end1()
	else: 
		print("I don't know what "+result6+" means. Please type a 1,2 or 3 or press control C to quit.")
		result5() 
#First ending and first minigame 

def end1(): 
	startrun = input('You must run away from the Yeti, once you press the 1 key a timer will start. You must input 10 characters one by one in less than 4 seconds to escape! \n\n>>') 

	if startrun == '1':
		start= time.time() 
		count=0
		
		while count < 10:  
			input('>>')
			count += 1

		end= time.time()
	
	else: 
		print("Thats not a 1! Please enter a 1 to start the game")
		end1()

	if (start-end)< 10: 
 		print("YOU HAVE OUTRUN THE YETI! You wander for a few more days and eventually find your way back to a ski trail. You're  Press control C to quit. Make sure to play again to explore all the multiple endings") 
	else: 
		ending1=input("You weren't quick enough! You lose! Press 1 to restart")

		if ending1 == 1: 
			start()

		else: 
			print("I don't know what "+ending1+" means. Please type a 1 to try again or press control C to restart")
			ending1=input("You weren't quick enough! You lose! Press 1 to restart")
			if ending1 == 1: 
				start()


#Second/Third ending and Second minigame
number =random.randrange(1,10)
def end2(): 
	
	guess = eval(input("The Yeti have offered you a chance to earn respect by guessing the secret artifiact. There are 10 objects to chose from. Enter a value from 1-10 and the Yeti will point to a higher or lower aritfiact.\n\n>>"))
	
	if guess == number:
		ending2()

	elif guess > number:
		print("The Yeti points to a lower artifact, guess again.")
		

	elif guess < number:
		print("The Yeti points to a higher artifact, guess again.")
		

	else:
		print("That doesn't seem like a number, Please guess again.")
		end2()
	
	end2()


def ending2(): 
	ending2restart = input("Congradulations! You have been accepted by the Yeti people. A few weeks pass and you have to make a decision. \n\n1) Attempt to escape\n2) Live out your days with the Yeti people \n\n>>")

	if ending2restart == '1': 

		ending2var=input("You plan you escape for weeks, but you are caught at the last second. The Yetis aren't happy at all with you decision and decide that if they can't have you no one can. Press 1 to restart or press control C to quit. \n\n>>" )
		
		if ending2var == "1": 
				start() 
		else: 
			print("I don't know what "+ending2var+" means, please enter a 1 or control C to quit")	
			ending2()

	elif ending2restart == '2': 
		print("You live out your days peacefully with the Yeti. You have reached the end of the game! Be sure to play again for multiple endings! Press control C to quit.")
	else: 
		print("I don't know what "+ending2restart+" means. Please type a 1 or a 2 or press control C to quit.")
		ending2() 

#Other ending/death 
def end3(): 
	ending3=input("You decide to try fight them off... it doesnt work\nPress 1 to restart.\n\n>>")
	if ending3 == '1':
		start()
	else: 
		print("I don't know what "+ending3+" means, enter a 1 to restart or press " )


start()


