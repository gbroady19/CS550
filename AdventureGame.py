def start():
	result = input("\n\n It all started with a simple ski trip, how could it have gone so terribly wrong? \n\nYou've been lost for a few hours now, trying to get back to the trail. It's getting dark. You see a gave where you can camp for the night, but your gut tells you the trail is right over the next hill \n\n 1) Go into the gave for the night \n2) Keep looking for the trail.\n\n>> ")

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
	result2 = input("You find some dry branches and start a small fire. Its not enough to keep you warm, but it is enough to keep you alive. The next morning you wake up")

