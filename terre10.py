#PRIME NUMBER

import sys
from terre_fonctions import EH_argument_lenght_and_is_digit, prime_number


# Part 1 : Error Handling and Parcing

EH_argument_lenght_and_is_digit(sys.argv[1:], 1)
number_to_test = int(sys.argv[1])


# Part 2 : Resolution and Display

prime_number(number_to_test)

