#The longest walk possible that still guarentees walking home more than 50% of the time is 14 blocks. 15 blocks sometimes results in walking home more than 50% of the time, but not always. 

#Broadly, monte carlo simulations use random sampling to obtain numerical results. Monte carlo simulations are used in three categoriesL optimization, numerical integration, and probablity distribution. They can be used in physics and math problems, and  are often used when other methods of simulations simply don't work well. They often work by defining an area, generating a random selection of points and then using data about the points to determine information. https://en.wikipedia.org/wiki/Monte_Carlo_method#Overview

import random
import sys
import math

n = int(sys.argv[1])


def dartthrow(n):
	dartcount = 0
	for i in range(n):
		x=random.randrange(0,3)
		y= random.randrange(0,3)
		if math.sqrt(abs((((0-y)^2)+(0-x)^2) <= 1)):
			dartcount +=1 
	
	number = (dartcount*4)/n
	print(number)

dartthrow(n)

# The number approaches 3.1, or apox. PI. From my reasearch I discovered that this is actually because the percent of the area that a circle radius one takes up in a 2 x 2 square is PI/4. 