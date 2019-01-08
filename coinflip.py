import random as r

data = [0 for x in range(11)]

for x in range(1000000):
	headcount = 0
	flips = 0 
	while flips < 10:
		side = r.randrange(0,2)
		if side == 0:
			headcount +=1
		flips +=1
	data[headcount]+=1
print(data)


