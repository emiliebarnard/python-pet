import pickle
from pathlib import Path

from pets import *


def main():
	print("Welcome to Python Pet!\nLoading...")
	
	# check for save file
	
	# later allow for different savefiles - maybe by the name of the pet - and have an interface to open up a specific one
	if Path("/savefile.dat").is_file():
		print("save file found")
	else:
		print("No save file found. A stranger in the night hands you an egg:")
		newPet = hatchPet()
		# newPet.printPet()


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