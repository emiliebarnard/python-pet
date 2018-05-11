class Pet():
	def __init__(self):
		self.petName = "Jemima"
		self.petType = "Egg"
	def printPet(self):
		print()
		print("?")
		print()


class Python(Pet):
	def __init__(self):
		self.petType = "Python"
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