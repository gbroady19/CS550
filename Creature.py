'''
Properties: Hunger, happiness, energym name, age 

Methods/functions: Run, bark, eat, sleep, play, bite 
'''
class Dog: 

	#constructor 
	#scale out of 10
	def __init__(self, name,energy,fullness): 
		self.fullness = fullness
		self.energy = energy
		self.happiness= 5
		self.name = name
	#Methods /functions 
	def play(self): 
		if self.energy > 0 and self.fullness > 0:
			self.happiness+=1
			self.fullness-=1
			self.energy-=1
			status = self.name+" played and it was fun."
		else: 
			status = "Erm, "+self.name+" can't play right now, maybe try a nap or some food!"
		return status

	def stats(self): 
		info = "\nName: " + self.name
		info  += "\nEnergy: " +str(self.energy)
		info  += "\nHappiness: " +str(self.happiness)
		info  += "\nFullness: " +str(self.fullness)

		return info 



dog1 = Dog("Big Dog",8,2) 
dog2 = Dog("Big Doggy",5,7)
# print(dog1.stats())
# print(dog2.stats())
# print(dog1.name)

while True:
	print(dog1.stats())
	choice = input("What would you like to do with your doggo?")
	if choice == "Play":
		print(dog1.play())
	else:
		print("You can't do that") 

# print(dog1.play())
# print(dog2.play())
# print(dog1.play())
# print(dog1.play())
# print(dog1.play())
# print(dog1.play())
# print(dog1.play())
# print(dog1.play())
# print(dog1.play())
# print(dog1.play())
# print(dog1.play())

# print(dog1.stats())
# print(dog2.stats())