

''' 1.
	Create a class, Point, that keeps track of two properties: x and y
	When a point is created, values for x and y should be provided.

	The methods for this class are as follows:
	rotate90: rotate the point 90° about the origin
	rotate180: rotate the point 180° about the origin
	rotaten90: rotate -90° about the origin
	translate: given 2 values, translate the point by the given amount.
	flip_horizontally: flip the point on the x-axis
	flip_vertically: flip the point on the y-axis
'''
# class Point:
# 	def __init__(x,y)
# 		self.x = x
# 		self.y = y

# def rotate90(self): 
# 	self.x = xtemp
# 	self.x = -(self.y) 
# 	self.y = xtemp 

# def rotate180(self): 
# 	self.x = -(self.x)
# 	self.y = -(self.y)

# def rotaten90(self):
# 	self.x = xtemp 
# 	self.x=self.y
# 	self.y = -xtemp 

# def translate(self,moveX,moveY):
# 	self.x = self.x + moveX
# 	self.y = self.y +moveY

# def flip_horizontally(self):
# 	self.y = -(self.y)

# def flip_vertically(self):
# 	self.x = -(self.x)
'''
	Create a class, student, that keeps track of four properties: energy, hunger, stress, and hours.
	These properties have a range from 0-100, except hours, which has a range from 0-24. 100 energy means they are energetic; 100 hunger means they are very hungry; 100 stress means they are extremely stressed. When you create a new student, assume they have moderate hunger, low stress, a lot of energy, and 24 hours.

	The methods for the student class are as follows:
	study: Given a value (to adjust hours), study for that given length of time. Studying decreases energy and increases hunger based on the length of the study.
	sports: Given a value (to adjust hours), play sports for that given length of time. This decreases energy, increases hunger, and decreases stress based on the length of the sports.
	class: Given a value (to adjust hours), attend classes for a given length of time. This decreases energy, increases hunger, and increases stress based on the length of the class.
	take_test: Given a value (to adjust hours), this increases stress. 
	submit_paper: this decreases stress.
	eat_meal: Given a value (to adjust hours), this decreases stress, decreases hunger, and increases energy.
	sleep: Given a time (to adjust hours), this decreases stress, increases energy, and increases hunger.
	new_day: resets the hours in a day.

	You may not l

	et a student do more than 24 hours worth of activities in a given day. 
'''
class Student:
	def __init__(energy,hunger,stress,hours):
		if energy > 100: energy = 100
		self.energy = energy 
		self.hunger = hunger 
		self.stress= stress
		self.hours=hours

def study(self,hours):
	if self.energy > 0 and self.hunger > 0 and self.hours > 0:
		self.energy += -(3* hours)
		self.hunger +=  (3 * hours)
		self.hours += -(hours)
	else:
		print("You can't do that right now")

def sports(self,hours):
	if self.energy > 0 and self.hunger > 0 and self.hours > 0:
		self.energy += -(4* hours)
		self.hunger +=  (4 * hours)
		self.stress += -(6*hours)
		self.hours += -(hours)
	else:
		print("You can't do that right now")


def gotoclass(self,hours):
	if self.energy > 0 and self.hunger > 0 and self.hours > 0:
		self.energy += -(4* hours)
		self.hunger +=  (4 * hours)
		self.stress += (6*hours)
		self.hours += -(hours)
	else:
		print("You can't do that right now")

def take_test(self,hours)
	if self.hours > 0:
		self.stress +=(7*hours)
		self.hours += -(hours)
	else:
		print("You can't do that right now")

def submit_paper(self):
	self.stress -= 15

def eat_meal(self,hours):
	if self.hours > 0:
		self.energy += +(4* hours)
		self.hunger +=  -(4 * hours)
		self.stress += -(6*hours)
		self.hours += -(hours)
	else:
		print("You can't do that right now")
def sleep(self,hours)
	if self.hours > 0:
		self.energy += (4* hours)
		self.hunger +=  (4 * hours)
		self.stress += -(6*hours)
		self.hours += -(hours)
	else:
		print("You can't do that right now")

def new_day(self):
	self.hours = 24 

	 






















