'''
	On this assignment, you should work with a partner. You must submit what you have completed at the end of the class period, but you do not need to complete any leftover problems for homework. 

	For some of these problems you will need to create a class; for others, you will need to use a library. 
	You do NOT need to put all your solutions in this file, however you should keep all your solutions together, clearly labeled with descriptive file names, in one folder. 
'''





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
class Point:
	def __init__(x,y):
		self.x = x
		self.y = y

def rotate90(self): 
	self.x = xtemp
	self.x = -(self.y) 
	self.y = xtemp 

def rotate180(self): 
	self.x = -(self.x)
	self.y = -(self.y)

def rotaten90(self):
	self.x = xtemp 
	self.x=self.y
	self.y = -xtemp 

def translate(self,moveX,moveY):
	self.x = self.x + moveX
	self.y = self.y +moveY

def flip_horizontally(self):
	self.y = -(self.y)

def flip_vertically(self):
	self.x = -(self.x)


''' 2.
	Create a class, Bicycle, that keeps track of three properties: cadence, gear, speed. 
	When a Bicycle is created, cadence, gear, and speed are accepted as arguments.

	The methods for this class are as follows:
	set_gear: given a value, set the gear to that value
	set_cadence: given a value, set the cadence to that value
	apply_brake: given a value, decrease the speed of the bike by that value
	speed_up: given a value, increase the speed of the bike by that value
'''

class Bicycle:
  def __init__(gear,cadence, speed):
        self.gear=gear
        self.cadence=cadence
        self.speed=speed
        
  def set_gear(value):
    self.gear=value
  def set_cadence(value):
    self.cadence=value
  def apply_brake(value):
    self.speed=speed-value
  def speed_up(value):
    self.speed=speed+value


''' 3.
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

	You may not let a student do more than 24 hours worth of activities in a given day. 
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




''' 4. 
	Use numpy to create an array of numbers going from 20 to 100 by increments of .25
	Then, multiply all the values in the array by 4. 
	Then. find the sum of all the values.
'''
#https://docs.sympy.org/latest/modules/geometry/points.html
import numpy as np
A=np.arange(20,100,.25)
print(A)
b=4*A
print(b)
print(np.sum(A))





''' 5.
	Use turtle to draw a star.
'''
from turtle import *
color('magenta')
while True:
    left(200)
    forward(300)
    if abs(pos()) < 1:
        break





''' 6.
	Use SymPy to determine the area of a triangle given points a, b and c.
'''
# https://docs.sympy.org/latest/modules/geometry/points.html
# https://docs.sympy.org/0.7.2/modules/geometry.html
from sympy.geometry import Triangle
# a, b, c = Point(5,22), Point(0, 0), Point(10, 0)

# base=b.distance(c)
# basepoint=
# height=a.distance(basepoint)
# area=.5*base*height
# print(area)

x = Point(0, 0)
y = Point(10, 0)
z = Point(5,22)
t = Triangle(x, y, z)
print(t.area)




''' 7. 
	Use VPython to build a 3D snowman.
'''




''' Sources:
	https://docs.oracle.com/javase/tutorial/java/javaOO/classes.html
'''