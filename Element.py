class Element: 
	def __init__(self,element,number,symbol,weight,boil,melt,density_vapour,fusion): 
		self.element = element
		self.number = number 
		self.symbol =symbol
		self.weight = weight
        self.boil = boil
        self.melt = melt
        self.density_vapour = density_vapour
        self.fusion = fusion
	
  def __str__(self):
    return "Element Name: "+self.element+"\nAtomic Symbol: "+self.symbol+"\n Atomic #: "+str(self.number)+ "\nAtomic Weight: "+str(self.weight)+"\nBoiling Point: "+str(self.boil)+"\nMelting Point: "+str(self.melt)+""
    

