class Choate Student: 

	#constructor 
	#scale out of 10
	def __init__(self, name,energy,fullness, happiness, workload, gpa, form, money): 
		self.fullness= fullness
		self.energy = energy
		self.time = energy 
		self.happiness= happiness
		self.homework = workload
		self.grades = gpa
		self.allowance = money
		self.name = name
		self.grade = form 
	#Methods /functions 
	def netflix(self): 
		if self.energy > 0 and self.fullness > 0:
			self.happiness+=4
			self.time+=-1
			self.energy+=-1
			self.grades +=-1
			status = self.name+" watched some Netflix and it was fun."
		else: 
			status = "Erm, "+self.name+" can't watch netflix right now, maybe get some homework or sleeping first"
		return status

	def stats(self): 
		info = "\nName: " + self.name
		info  += "\nEnergy: " +str(self.energy)
		info  += "\nHappiness: " +str(self.happiness)
		info  += "\nFullness: " +str(self.fullness)

		return info 
	def sleep():
		self.energy+= 4
		self.grades += -1
		self.time+=-2 
		self.happiness+=2




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
