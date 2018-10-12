import sys 
ui = list((sys.argv[1]))
eightcount = 0

def crzy8(ui):
	global eightcount
	if ui[ui.index(8)]:
		if ui[ui.index(8)-1] == 8:
			eightcount +=2
			crzy8(ui)
		else: 
			eightcount +=1 

	return eightcount

print(crzy8(ui))
