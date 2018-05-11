import math

class Pet():
	def __init__(self):
		self.name = "Jemima"
		self.type = "Egg"
		self.xp = 0
		self.level = 0
	def printPet(self):
		print()
		print("(?)")
		print()
	def xpIncrease(self, changeInXp):
		self.xp += changeInXp
		oldLevel = self.level
		self.level = math.floor(self.xp/1000) # this factor may need to change
		if self.level > oldLevel:
			print("Level up!")


class Python(Pet):
	def __init__(self):
		Pet.__init__(self)
		self.type = "Python"
	def printPet(self):
			print()
			print("/\/(8)-<")
			print()	

x = Pet()
x.printPet()
print(x.petType)

y = Python()
y.printPet()
print(y.petType)
print(y.petName)