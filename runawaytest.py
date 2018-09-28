
import time 


def test():
	startrun= input("You must run away from the Yeti, once you press the 1 key a time will start. You must input 10 characters in less than 10 seconds to escape! \n\n>>") 

	if startrun == '1':
		start= time.time() 
		count = 0 
		
		while count < 10:  
			input('>>')  
			count += 1

		end= time.time()
	else: 
		print("Thats not a 1! Please enter a 1 to start the game")

	if (start-end) < 10 : 
		print("YOU WIN! PRESS")

	else:
		print('you lose!') 

test() 