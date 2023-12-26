# COUNT THE NB OF CARACTERS IN A STRING

import sys
from terre_fonctions import EH_argument_lenght, EH_string_not_only_digit


# Part 1 : Slicing and Error Handling

arg = sys.argv[1:]
EH_argument_lenght(arg, 1)
arg_string = "".join(arg)
EH_string_not_only_digit(arg_string)


# Part 2 : Resolution
    
counter = 0
for i in arg_string:
    counter += 1


# Part 3 : Display

print(counter)