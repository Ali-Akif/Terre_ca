# DISPLAY THE RESULT AND THE REMAIN OF A DIVISION

import sys
from terre_fonctions import EH_argument_is_digit, result_remain


# Part 1 : Error Handling

EH_argument_is_digit(sys.argv[1:], 2)


# Part 2 : Slicing

a, b = int(sys.argv[1]), int(sys.argv[2])


# Part 3 : Resolution and display

result_remain(a, b)

