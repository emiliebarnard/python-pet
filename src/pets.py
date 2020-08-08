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
		self.base_xp = 10
		self.exponent = 1.8
		self.xp_to_next_level = 0
		self.display = "(?)"
		self.food_num = 0 # 0 being the least amount of food fed
		self.food_factor = 0 # scales how much food the pet needs, depending on species
		self.max_food = 0 # the max number of food the pet can eat, default is 0

	# kwargs is a dict of the keyword args passed to the function
	# allows for testing using an optional pet = parameter
	@staticmethod
	def hatch(**kwargs):
		print("\n(?)\n")
		input("Press Enter to hatch your egg ")
		print("Your egg is hatching...")
		sleep(3)
		if kwargs: # for testing:
			pet_choice = kwargs["pet"]
		else: # standard use case
			pet_options = ["Python", "Cat"]
			pet_choice = choice(pet_options)
		return eval(pet_choice + "()")
	def print_pet(self):
		print("\n" + self.display + "\n")
	def show_stats(self):
		self.print_pet()
		col_width = len("XP to next level:")
		print("------ " + self.name + "'s stats: ------")
		print("%s %s" % (("Type:").ljust(col_width), self.type))
		print("%s %d" % (("Level:").ljust(col_width), self.level))
		print("%s %d" % (("XP:").ljust(col_width), self.xp))
		print("%s %d" % (("XP to next level:").ljust(col_width), self.xp_to_next_level))
		print("%s %s" % (("Hunger:").ljust(col_width), self.get_hunger().title()))
		print(self.level)
	def xp_increase(self, change_in_xp):
		self.xp += change_in_xp
		#old_level = self.level
		#self.level = floor(self.xp/(exp(self.level) + 10)) # may need to edit this function
		## bug: this doesn't work properly if you go up multiple levels at once
		#if self.level > old_level:
			#self.level_up()
	def level_up(self):
			print("Level up!")
			self.set_level(self.level  + 1)
			#print("Congratulations, " + self.name + " is now level " + str(self.level) +"!")
	def set_level(self, new_level):
			self.level = new_level
			print(new_level)
			print(self.level)
			self.xp_to_next_level = floor(self.base_xp * (self.level ** self.exponent)) ## TODO: change leveling factor based on species?
			self.max_food = self.level * self.food_factor
			print("Congratulations, " + self.name + " is now level " + str(self.level) +"!")
	def rename(self):
		self.name = input("What would you like to name your " + self.type + "? ")
		print("Your " + self.type + "'s new name is " + self.name)
	def get_hunger(self):
		# three levels: starving, hungry, stuffed
		hunger_text_options = ["starving", "hungry", "stuffed"]
		## TODO: add more hunger levels
		if self.food_num < self.max_food / len(hunger_text_options):
			return "starving"
		elif self.food_num < self.max_food * 2 / len(hunger_text_options):
			return "hungry"
		else:
			return "stuffed"


class Python(Pet):
	def __init__(self):
		Pet.__init__(self)
		self.type = "Python"
		self.food_factor = 3
		self.display = "/\/(8)-<"



#   /^-——^\
# ==\=‘.’=/==
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
		self.food_factor = 6
		self.display = "    /^-——^\\\n    \\=‘.’=/\n   /       \\\n  |         |\n   \\__  ___/\n      \\ \\\n       \\ \\\n       / /\n       \\/"
