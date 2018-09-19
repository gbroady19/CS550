while True: 
	try: 
		num=float(input("Pick a number between 1 and 5\n\n>>"))
		while num<1 or num >5:
			num = int(input('Thats not in the range! try again! \n\n>>'))
		print("Sucess!")
		break
	except ValueError: 
			print("thats not a number")