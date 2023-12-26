#EVEN OR ODD

import sys
from terre_fonctions import EH_argument_is_digit, even_odd


# Part 1 : Slicing

arg = sys.argv[1:]


# Part 2 : Error Handling

EH_argument_is_digit(arg, 1)


# Part 3 : Resolution and display

number = int("".join(arg))
even_odd(number)

