# SQUARE ROOT OF A POSITIVE INTEGER

import sys
from terre_fonctions import EH_argument_lenght_and_is_digit, sqrt_positive_int


# Part 1 : Parcing and Error Handling

arg = sys.argv[1:]
EH_argument_lenght_and_is_digit(arg, 1)
radicant = int(arg[0])

# Part 2 : Resolution and Display

sqrt_positive_int(radicant)

