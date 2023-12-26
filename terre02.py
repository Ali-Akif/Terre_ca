# PRINT GIVEN ARGUMENTS LINE BY LINE

import sys


# Part 1 : Functions
def arguments_printer ():
    """
    Prints the given arguments line by line.
    
    Return:
        str : arguments
    """
    arguments = [i for i in sys.argv[1:]]

    for arg in arguments:
        print(arg)


# Part 2 : Display
arguments_printer()
