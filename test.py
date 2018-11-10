### Unit testing for code

from src.pets import *

# test 1
pet1 = Pet()
pet1.print_pet()
print(pet1.type)

# test 2
pet2 = Python()
pet2.print_pet()
print(pet2.type)
print(pet2.name)
pet2.xp_increase(12)