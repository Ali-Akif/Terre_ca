# REVERSE A STRING

import sys
from terre_fonctions import EH_argument_lenght, reverse_string


# Part 1 : Parcing

arg = sys.argv[1:]


# Part 2 : Error Handling

EH_argument_lenght(arg, 1)


# Part 3 : Resolution and display

string = "".join(arg)
reverse_string(string)

