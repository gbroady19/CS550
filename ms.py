#minesweeper 

import sys 
import random
 
height = int(sys.argv[1])+2
width = int(sys.argv [2])+2
bombs = int(sys.argv [3])

solution = [[0] * (width) for x in range(height)]
userboard = [["□"] * (width) for x in range(height)]
#from https://www.compart.com/en/unicode/U+25A1
checkcoordinates = [0][0]
flagcount = 0 
checklist =[]

def printboard(): 
	for x in range(1,len(userboard)-1):
		for y in range(1,len(userboard[0])-1):
			print(userboard[x][y],end=" ")
		print("")
	selecttile()

def selecttile(): 
	global coordinates
	global flagcount
	userinput = input("Press F to place a flag, Press C to clear\n\n>>")
	if userinput == "F": 
		tileselection= input("Enter two corodinates separated by commas: ")
		flag_input= tileselection.split(',')
		flagcoordinates = [int(x.strip()) for x in flag_input]
		userboard[flagcoordinates[0]][flagcoordinates[1]] = "F"
		flagcount += 1 
		printboard() 

	if userinput == "C":
		tileselection= input("Enter two corodinates separated by commas: ")
		tile_input= tileselection.split(',')
		coordinates = [int(x.strip()) for x in tile_input]
		userboard[coordinates[0]][coordinates[1]] = solution[coordinates[0]][coordinates[1]] 
		bombchecking()

def bombchecking(): 
	if userboard[coordinates[0]][coordinates[1]] == "*":
		print("""That was a BOMB, you lose""")
#https://asciiart.website/index.php?art=objects/explosives
		quit()

	elif userboard[coordinates[0]][coordinates[1]] == 0:
		checklist.append(coordinates[0])
		checklist.append(coordinates[1]) 

		zeroreveal()

	else: 
		printboard()

def zeroreveal():
	
	while len(checklist) > 0:
		coordinate1 = checklist[0]
		coordinate2 = checklist[1]
		checklist.pop(0)
		checklist.pop(0)

		for x in range(-1, 2):
			for y in range(-1, 2):
				if solution[coordinate1 + (x)][coordinate2+(y)] == 0: 
					if solution[coordinate1+(x)][coordinate2+(y)] != userboard[coordinate1+(x)][coordinate2+(y)]:
						checklist.append(coordinate1+x)
						checklist.append(coordinate2+y)
						userboard[coordinate1+(x)][coordinate2+(y)]=  solution[coordinate1+(x)][coordinate2+(y)]
					else: 
						pass 
				else: 
					userboard[coordinate1+(x)][coordinate2+(y)]=  solution[coordinate1+(x)][coordinate2+(y)] 
		zeroreveal()
		
		printboard()

				








# def continuouscheck(x,y):
# 	print(x,y)
# 	if 0<x<width-1 and 0<y<height-1: #onboard
# 		if solution[x+1][y] == 0: # is a zero
# 			if solution[x+1][y] == userboard[x+1][y]: # is already revealed
# 				print("nope") 
# 			else: #not revealed
# 				userboard[x+1][y] = solution[x+1][y] # reveal
# 				print("leave recursion 1") 	
# 				continuouscheck(x+1,y) # check around
# 				print("return recursion 1")
# 		else: 
# 			solution[x+1][y]=userboard[x+1][y]

# 		if solution[x][y+1] == 0:
# 			if solution[x][y+1] == userboard[x][y+1]:
# 				print("nope")
# 			else:  
# 				userboard[x][y+1] = solution[x][y+1] 
# 				print("leave recursion 2") 	
# 				continuouscheck(x,y+1)
# 		else: 
# 			userboard[x][y+1] = solution[x][y+1] 
		
# 		if solution[x+1][y+1] == 0:
# 			if userboard[x+1][y+1] == solution[x+1][y+1]:
# 				print("nope") 
# 			else:
# 				userboard[x+1][y+1] = solution[x+1][y+1]
# 				print("leave recursion 3") 	
# 				continuouscheck(x+1,y+1)
# 		else: 
# 			userboard[x+1][y+1] = solution[x+1][y+1] 

# 		if solution[x-1][y] == 0:
# 			if userboard[x-1][y] == solution[x-1][y]:
# 				print("nope")
# 			else: 
# 				userboard[x-1][y] = solution[x-1][y] 
# 				print("leave recursion 4") 	
# 				continuouscheck(x-1,y)	

# 		else: 
# 			userboard[x-1][y] = solution[x-1][y] 
			
		
# 		if userboard[x-1][y-1] == 0: 
# 			if solution[x-1][y-1]== userboard[x-1][y-1]:
# 				print("nope")
# 			else:
# 				solution[x-1][y-1]= userboard[x-1][y-1]
# 				print("leave recursion 5") 	
# 				continuouscheck(x-1,y-1)
		
# 		else: 
# 			solution[x-1][y-1]= userboard[x-1][y-1]

# 		if userboard[x][y-1] == 0:
# 			if solution[x][y-1]== userboard[x][y-1]: 
# 				print("nope") 
# 			else: 
# 				solution[x][y-1]= userboard[x][y-1]
# 				print("leave recursion 6") 	
# 				continuouscheck(x,y-1)
# 		else: 
# 			solution[x][y-1]= userboard[x][y-1]


# 		if userboard[x+1][y-1] == 0:
# 			if solution[x+1][y-1]== userboard[x][y-1]: 
# 				print("nope") 
# 			else: 
# 				solution[x+1][y-1]= userboard[x][y-1]
# 				print("leave recursion 7") 	
# 				continuouscheck(x+1,y-1)
# 		else: 
# 			solution[x+1][y-1]= userboard[x+1][y-1]


# 		if userboard[x-1][y+1] == 0:
# 			if solution[x-1][y+1]== userboard[x][y-1]: 
# 				print("nope") 
# 			else: 
# 				solution[x-1][y+1]= userboard[x][y-1]
# 				print("leave recursion 8") 	
# 				continuouscheck(x-1,y+1)
# 		else: 
# 			solution[x-1][y+1]= userboard[x-1][y+1]

# 	printboard()


for x in range(bombs):
	solution[int(random.randrange(1, height
-1))] [int(random.randrange(1,width-1))] = '*'

solution[0] = [1]*(width) 
solution[-1] = [1]*(width)

for j in solution: 
	j[0]= 1
	j[-1]= 1



for x in range(1,height-1):
	for y in range(1,width-1):  

		if solution[x][y] == "*": 
			if solution[x-1][y-1] != "*": 
				solution[x-1][y-1] += 1 
			if solution[x][y-1] != "*": 
				solution[x][y-1] +=1 
			if solution[x+1][y-1] != "*": 
				solution[x+1][y-1] +=1
			if solution[x-1][y] != "*":
				solution[x-1][y] +=1
			if solution[x+1][y] != "*":
				solution[x+1][y] +=1
			if solution[x-1][y+1] != "*":
				solution[x-1][y+1] +=1
			if solution[x][y+1] != "*":
				solution[x][y+1] +=1
			if solution[x+1][y+1] != "*":
				solution[x+1][y+1] +=1


printboard()

#Much help from Anan Aramthanapon 








# https://www.tutorialspoint.com/python/python_2darray.htm
#https://stackoverflow.com/questions/7378091/taking-multiple-inputs-from-user-in-python




