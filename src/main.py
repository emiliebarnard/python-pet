import pickle
from pathlib import Path
from random import choice

from pets import Pet


def main():
	print("Welcome to Python Pet!\nLoading...")
	
	# check for save file
	
	# TO-DO: later allow for different savefiles
	# maybe have the user select the save name with defaulted to the name of the pet
	# have an interface to open up a specific one
	
	if Path("/savefile.dat").is_file():
		print("save file found")
	else:
		subjects = ["A stranger in the night", "A wild Skitty appears and", "Some rando", "An unladen swallow flies by and somehow"]
		print("No save file found. " + choice(subjects) + " hands you an egg:")
		
		# newEgg = Pet()
		# petType = newEgg.hatch()
		# petType = Pet.hatch()
		# ourPet = eval(pet_type + "()")
		our_pet = Pet.hatch()
		our_pet.print_pet()
		print("Congratulations! Your new " + our_pet.type + " Pet has hatched!")
		our_pet.rename()
		#print(ourPet.name)
		
		
		# newPet.printPet()

# Only runs if this was the file run as the main module
if __name__ == "__main__":
	main()



# testing
# x = Pet()
# x.printPet()
# print(x.type)
# 
# y = Python()
# y.printPet()
# print(y.type)
# print(y.name)
# y.xpIncrease(12)
