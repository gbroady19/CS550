import random
import sys

n = int(sys.argv[1])


def walking(n):
	walkcount =0
	for y in range(n): 
		location=[0,0]
		for x in range(22):
			direction = random.randrange(0,4)
			if direction == 0: 
				location[0] = location[0] + 1
			if direction == 1:
				location[0] = location[0] - 1 
			if direction == 2: 
				location[1]= location[1] +1
			if direction == 3:
				location[1] = location[1]-1


		blockh = abs(int(location[0])) + abs(int(location[1]))

		if blockh <= 4:
			walkcount +=1
		
		
	print(str((walkcount/n)*100)+'%')

walking(n)



