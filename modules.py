import random 
# from random import randint
# print(random.random())

# print(random.randrange(10, 100))
# print(random.randint(10, 100))

# print(dir(random))

import customModule
import termcolor
import pyfiglet

print(dir(pyfiglet))
print(dir(termcolor))
print(pyfiglet.figlet_format('BOB'))
print(termcolor.colored(pyfiglet.figlet_format('BOB'), color='red'))
# print(dir(customModule))
customModule.myFunc('bob')

