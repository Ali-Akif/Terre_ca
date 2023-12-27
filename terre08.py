# POWER

import sys
from terre_fonctions import EH_argument_lenght, EH_argument_is_digit, power


# Part 1 :Parcing and Error Handling 

arg = sys.argv[1:]
EH_argument_is_digit(arg, 2)
base = int(arg[0])
exponent = int(arg[1])


# Part 2 : Resolution and Display

power(base, exponent)
