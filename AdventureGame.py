from timeit import default_timer as timer
def start():
	result = input("\n\n It all started with a simple ski trip, how could it have gone so wrong? \n\nYou've been lost for a few hours now, trying to get back to the trail. It's getting dark. You see a gave where you can camp for the night, but your gut tells you the trail is right over the next hill. Your next decision might determine your fate \n\n1) Go into the cave for the night \n2) Keep looking for the trail.\n\n>> ")
	if result == '1':
		cave()
	elif result == '2':
		death1()

	else:
		print("I don't know what "+result+" means. Please type a 1 or a 2.")
		start()
	
def death1(): 
	restart1 = input("You follow your instinct and continue searching for the trail home. It gets darker and darker, colder and colder. You don't survive the night. Press 1 to restart \n >>")
	if restart1 == '1': 
		start() 
	else: 
		print("I don't know what "+restart1+" means. Please type a 1")
		death1() 

def cave():
	result2 = input("You find some dry branches and start a small fire. Its not enough to keep you warm, but it is enough to keep you alive. The next morning you wake up parched. The snow looks so tempting to eat just as it is. \n1) Put snow directly in your mouth \n2) Rekindle the fire and melt the snow before drinking \n\n >>")
	
	if result2 == '2':
		food1() 
	elif result2 == '1':
		death2() 
	else: 
		print("I don't know what "+result2+" means. Please type a 1 or a 2")
		cave() 

def death2():
	restart2 = input("You eat what seems like bucket fulls of snow, but the thirstiness never seems to go away. You lay down in the snow and relax. You decide to rest your eyes for a few minutes... which turns into forever \n enter 1 to restart \n\n>>")

	if restart2 == '1':  
		start()
	else:  
		print("I don't know what "+restart2+" means. Please type a 1")
		death2() 

def food1(): 
	result3 =input("You drink the water and feel refreshed enough to go search for some food. You see two sets of tracks going in two different directions. One set is small with two toes visible. The other is larger, with four toes. You have a small calibar hunting rifle that your friend suggested you bring along as your only weapon/ Do you follow the large animal for a bigger meal or the smaller one for easier prey \n\n1) Follow the larger tracks \n2) Follow the smaller tracks \n\n>>")
	
	if result3 == '1':
		death3() 
	elif result3 == '2':
		result4()

def death3(): 
	restart3 = input("You follow the tracks until you see something large rushing towards you. You fire your weapon it does nothing. You're no match for the bear. Enter 1 to restart \n\n >>")
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
	result5 = input("The path lead you to a clearing filled with ") 
 
def end1(): 
startrun= input('You must run away from the Yeti, once you press the 1 key a time will start. You must input 10 characters in less than 10 seconds to escape! \n\n>>') 

if startrun = '1':
	start= timer() 
	count=0
	while count < 10:  
		intput('>>')  
		count += 1

	end= timer()
else: 
	print("Thats not a 1! Please enter a 1 to start the game")

if (start-end)> 10: 
 	ending1= input("YOU WIN! PRESS") 


start()
