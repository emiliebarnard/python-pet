### Unit testing for code

from src.pets import *


test_num = 1
line_break = "####################"

# start test
print("\n\nTest " + str(test_num) + ": Pet creation\n" + line_break)
pet = Pet()
pet.print_pet()
print(pet.type)
# set up for next test
pet = None
test_num += 1

# start test
print("\n\nTest " + str(test_num) + ": XP increase\n" + line_break)
pet = Python()
pet.print_pet()
print(pet.type)
print(pet.name)
pet.xp_increase(12)
# set up for next test
pet = None
test_num += 1

# start test
print("\n\nTest " + str(test_num) + ": Random hatch\n" + line_break)
pet = Pet.hatch()
pet.print_pet()
# set up for next test
pet = None
test_num += 1

# start test
print("\n\nTest " + str(test_num) + ": Python hatch\n" + line_break)
pet = Pet.hatch(pet = "Python")
pet.print_pet()
# set up for next test
pet = None
test_num += 1

# start test
print("\n\nTest " + str(test_num) + ": Cat hatch\n" + line_break)
pet = Pet.hatch(pet = "Cat")
pet.print_pet()
# set up for next test
pet = None
test_num += 1

