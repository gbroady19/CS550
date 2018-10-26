import random

class BankAccount:
	def __init__(PIN, balance,name,status): 
		self.accountnum = random.randrange(1000,10000)
		self.PIN = PIN 
		self.balance = balance
		self.status = status 
		self.name = name

	def deposit(self, deposit):
		self.balance += deposit 
		status = "Hello, "+self.name+" you have sucessfully deposited "+deposit+" your new balance is "+self.balance+""
		return status 

	def withdraw(self,withdraw): 
		if self.balance > withdraw: 
			self.balance += -withdraw
			status = "Hello, "+self.name+" you have sucessfully deposited "+withdraw+" your new balance is "+self.balance""
		return status 

	def stats(self): 
		info = "\nName: " + self.name
		info  += "\nBalance: " +str(self.balnce)
		info  += "\nStatus: " +str(self.happiness)
		return info 

def createaccount(PIN,name,balance): 
	bankaccount1=