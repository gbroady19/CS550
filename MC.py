'''
Monte Carlo Simulation Project for CS550 by Knute Broady
1/16/18
 
In this project, I attempt to use a monte carlo simulations to determine the average time spent tightening screws by a robotics team member. The results and justifcation for the numbers included will be outlined in a seperate docuement 

On my honor, I have neither given nor recieved unauthrized aid.
- KB 
'''

import random
import matplotlib.pyplot as plt 
import sys
n = int(sys.argv[1])


data = [0 for x in range(15)]
x = [i+1 for i in range(15)]

 
def time(n):
	for k in range(n):
		totaltime = 0
		projects = random.randrange(1,20)
		for x in range(projects):
			screws = random.randrange(2,70)
			for y in range(screws):
				turns = random.randrange(5,50)
				for z in range(turns):
					time = random.randrange(1,3)
					totaltime +=time
		totaltime = int(totaltime/3600)
		data[totaltime]+=1 

time(n)
plt.bar(x,data)
plt.show()


