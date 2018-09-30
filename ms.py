#minesweeper 

import sys 
import random

length = int(sys.argv[1])
width = int(sys.argv [2])
bombs = int(sys.argv [3])

a = [[0] * width for x in range(length)]



for x in range(bombs):
	a[int(random.randrange(0, length))] [int(random.randrange(0,width))] = '*'
	
for x in range(len(a)): 
	print(*a[x])


for x in range(length):
	bombcount= 0 
	for y in range(width):  
		if a [x] == "*": 
			pass 

		elif x == 0 and y == 0: 
			if a[x+1][y] == "*": 
				bombcount += 1 
			if a[x][y-1] == "*":
				bombcount +=1 
			
		elif x == 0 and y == (width): 
			if a[x+1][y] == "*": 
				bombcount += 1 
			if a[x][y-1] == "*":
				bombcount +=1 

		elif x == (length) and y == 0: 
			if a[x-1][y] == "*":
				bombcount += 1 
			if a[x][y-1] == "*":
				bombcount +=1 
		elif x == (length) and y == (width): 

			if a[x-1][y] == "*":
				bombcount += 1 
			if a[x][y-1] == "*":
				bombcount +=1 

		elif x == 0 and y !== 0 or (width): 
			if a[x+1][y] == "*": 
				bombcount += 1 

			if a[x][y+1] == "*":
				bombcount +=1 
			
			if a[x][y-1] == "*":
				bombcount +=1 

		elif x == (length) and y !== 0 or (width): 

			if a[x-1][y] == "*":
				bombcount += 1 
			
			if a[x][y+1] == "*":
				bombcount +=1 
			
			if a[x][y-1] == "*":
				bombcount +=1 

	 	elif y == (width) and x !== 0 or (length):
			if a[x+1][y] == "*": 
				bombcount += 1 
			
			if a[x-1][y] == "*":
				bombcount += 1 
			
			if a[x][y+1] == "*":
				bombcount +=1 

		elif y== 0 and x !== 0 or (length):

			if a[x][y-1] == "*":
				bombcount +=1 
			if a[x+1][y] == "*": 
				bombcount += 1 
			
			if a[x-1][y] == "*":
				bombcount += 1 



		else: 
			if a[x+1][y] == "*": 
				bombcount += 1 
			
			if a[x-1][y] == "*":
				bombcount += 1 
			
			if a[x][y+1] == "*":
				bombcount +=1 
			
			if a[x][y-1] == "*":
				bombcount +=1 
	a[x][y] = bombcount









# https://www.tutorialspoint.com/python/python_2darray.htm




