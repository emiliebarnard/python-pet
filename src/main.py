import pickle
from pathlib import Path
from random import choice

from pets import Pet

VERSION = 1.0


def main():
	print("Welcome to Python Pet!\nLoading...")

	# check for save file
	if not open_file():
		our_pet = hatch_egg()

	# run game menu
	# dictionary of commands, key is command, value is the definition of the command
	# placing this here for now in case the commands expand as you level up
	commands = {
		"exit" : "Exit from the game menu.",
		"nom" : "Feed your Python Pet.",
		"play" : "Play with your Python Pet.",
		"rename" : "Rename your Python Pet.",
		"stats" : "Shows a summary of your Python Pet."
	}
	game_menu(commands, our_pet)



# checks for a save file, returns boolean showing if file is found
# TO-DO: later allow for different savefiles
# maybe have the user select the save name with defaulted to the name of the pet
# have an interface to open up a specific one
def open_file():
	if Path("/savefile.dat").is_file():
		print("save file found")
		return True
	else:
		return False

def hatch_egg():
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
	return our_pet

# TO DO: also add main menu where you load/save files
def game_menu(commands, our_pet):
	user_entry  = ""
	while user_entry != "exit":
		print("type 'help' for commands")
		our_pet.print_pet()
		user_entry = input(">>> ").lower()
		if user_entry == "exit":
			break
		elif user_entry == "help":
			show_commands(commands)
		elif user_entry == "rename":
			our_pet.rename()
		elif user_entry == "stats":
			print("STUB STATS")




def show_commands(commands):
	title = "------ Python Pet, version " + str(VERSION) + " ------"
	print(title)
	print("Author:  Emilie Barnard")
	print("Website: emilie.codes")
	print()
	print("Type 'help' to see this list.")
	#print("Type 'help name' to find out more about the command 'name'.")
	print()
	col_width = max(map(len,commands)) + 1
	for command in sorted(commands.keys()):
		print("%s %s" % ((command + ":").ljust(col_width), commands[command]))
		# print(col_width)
	print("-" * len(title))


# Only runs if this was the file run as the main module
if __name__ == "__main__":
	main()



#testing
x = Pet()
x.print_pet()
print(x.type)
print(x.name)
x.xp_increase(12)
