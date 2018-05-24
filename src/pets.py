from math import floor, exp
from random import choice
from time import sleep



## move this into the Pet class	

class Pet():
	def __init__(self):
		# self.hatch()
		self.name = "Jemima"
		self.type = "Egg"
		self.xp = 0
		self.level = 0
	@staticmethod
	def hatch():
		print("\n(?)\n")
		input("Press Enter to hatch your egg ")
		print("Your egg is hatching...")
		sleep(3)
		petOptions = ["Python"]
		petChoice = choice(petOptions)
		return eval(petChoice + "()")
	def printPet(self):
		print()
		print("(?)")
		print()
	def xpIncrease(self, changeInXp):
		self.xp += changeInXp
		oldLevel = self.level
		self.level = floor(self.xp/(exp(self.level) + 10)) # may need to edit this function		
		## bug: this doesn't work properly if you go up multiple levels at once
		if self.level > oldLevel:
			self.levelUp()
	def levelUp(self):
			print("Level up!")
			print("Congratulations, " + self.name + " is now level " + str(self.level) +"!")


class Python(Pet):
	def __init__(self):
		Pet.__init__(self)
		self.type = "Python"
		
	def printPet(self):
			print()
			print("/\/(8)-<")
			print()	
