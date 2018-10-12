

ui = list(input("Put in a string, i'll tell ya how many x's are in there\n\n>>"))
counts = 0 

def count(ui):
	global counts
	try:
		del ui[ui.index("x")]
		counts += 1
		count(ui)
	except ValueError:
		pass
	return counts 

print(count(ui)) 
