import random
import sys
import matplotlib.pyplot as plt 

n = int(sys.argv[1])
data = [0 for x in range(52000)]
x = [i+1 for i in range(52000)]

def party(n):
	
	for y in range(n): 
		total = 0
		partynum= random.randrange(1,14)
		for z in range(partynum):
			servings = random.randrange(1,9)
			for i in range(servings):
				calories = random.randrange(40,501)
				total+= calories
		data[total]+=1
	

party(n)

plt.bar(x, data)
plt.show()




