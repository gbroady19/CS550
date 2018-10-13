#minesweeper for CS550 by KB. Completed 10/12/18 
# Sources consulted: https://www.tutorialspoint.com/python/python_2darray.htm
#https://stackoverflow.com/questions/7378091/taking-multiple-inputs-from-user-in-python
#MUCH help and suggestions provided by Anan Aramthanapon 
#Also help from Kevin Xie 
# please start by inputting ms.py height width bombs



import sys 
import random
 
height = int(sys.argv[1])+2 #height and width input from user 
width = int(sys.argv [2])+2
bombs = int(sys.argv [3])

solution = [[0] * (width) for x in range(height)] #board creation 
userboard = [["□"] * (width) for x in range(height)]

checkcoordinates = [0][0] #Creation of list 
flagcount = 0
checklist =[]




def wincheck(): #Checks if you've won after every revealing sequence 
	winchecking = 0
	for x in range(1,height-1):
		for y in range(1,width-1):
			if userboard[x][y] == "□":
				if solution[x][y] != "*":
					winchecking = 1
	if winchecking == 0:
		print("You WIN!")
		winboard()
	else: 
		printboard()


def winboard(): #Prints a board so you can see that you've won 
	solution = userboard
	for x in range(1,len(userboard)-1):
		for y in range(1,len(userboard[0])-1):
			print(userboard[x][y],end=" ")
		print("")
	quit()

def printboard(): 
	for x in range(1,len(userboard)-1): #prints board for other purposes
		for y in range(1,len(userboard[0])-1):
			print(userboard[x][y],end=" ")
		print("")
	selecttile()

def selecttile(): #allows user to select tile for flagging or clearing 
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

	if userinput == "C": #Allows user to clear spaces, sends to bombchecking
		global revealed
		tileselection= input("Please Enter the coordinate  Y,X format\n\n>>")
		tile_input= tileselection.split(',')
		coordinates = [int(x.strip()) for x in tile_input]
		if userboard[coordinates[0]][coordinates[1]] != solution[coordinates[0]][coordinates[1]]:
			userboard[coordinates[0]][coordinates[1]] = solution[coordinates[0]][coordinates[1]] 
			
			bombchecking()
		else: 
			print("That tile has already been selected")

	else: 
		print("I don't know what that means")
		selecttile()

def bombchecking(): #checks if user input was a bomb, if checks if it's a zero, if not sends to zero checkings
	if userboard[coordinates[0]][coordinates[1]] == "*":
		print("That was a BOMB, you lose")
		quit()

	elif userboard[coordinates[0]][coordinates[1]] == 0:
		checklist.append(coordinates[0])
		checklist.append(coordinates[1]) 

		zeroreveal()

	else: 
		wincheck()
	

def zeroreveal(): #if userinput was a zero, reveal all spaces around it, do the same for all zero it finds 
	global revealed
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
					userboard[coordinate1+(x)][coordinate2+(y)]=  solution[coordinate1+(x)][coordinate2+(y)] 

		zeroreveal()
		wincheck()

			

for x in range(bombs): #bomb placement
	solution[int(random.randrange(1, height-1))] [int(random.randrange(1,width-1))] = '*'

#boarder of ones to avoid index errors
solution[0] = [1]*(width) 
solution[-1] = [1]*(width)

for j in solution: 
	j[0]= 1
	j[-1]= 1


#creation of initial solution boards
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













