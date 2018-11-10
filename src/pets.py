from math import floor, exp
from random import choice
from time import sleep


class Pet():
	def __init__(self):
		# self.hatch()
		self.name = "Jemima"
		self.type = "Egg"
		self.xp = 0
		self.level = 0
		self.display = "(?)"
	@staticmethod
	def hatch():
		print("\n(?)\n")
		input("Press Enter to hatch your egg ")
		print("Your egg is hatching...")
		sleep(3)
		pet_options = ["Cat"]
		pet_choice = choice(pet_options)
		return eval(pet_choice + "()")
	def print_pet(self):
		print("\n" + self.display + "\n")
	def xp_increase(self, change_in_xp):
		self.xp += change_in_xp
		old_level = self.level
		self.level = floor(self.xp/(exp(self.level) + 10)) # may need to edit this function		
		## bug: this doesn't work properly if you go up multiple levels at once
		if self.level > old_level:
			self.level_up()
	def level_up(self):
			print("Level up!")
			print("Congratulations, " + self.name + " is now level " + str(self.level) +"!")
	def rename(self):
		self.name = input("What would you like to name your " + self.type + "? ")
		print("Your " + self.type + "'s new name is " + self.name)


class Python(Pet):
	def __init__(self):
		Pet.__init__(self)
		self.type = "Python"
		self.display = "/\/(8)-<"

  
#   /^-——^\ 
#   \=‘.’=/ 
#  /       \
# |         |
#  \__  ___/
#     \ \
#      \ \
#      / /
#      \/
  

class Cat(Pet):
	def __init__(self):
		Pet.__init__(self)
		self.type = "Cat"
		self.display = "    /^-——^\\\n    \\=‘.’=/\n   /       \\\n  |         |\n   \\__  ___/\n      \\ \\\n       \\ \\\n       / /\n       \\/"
