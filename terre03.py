# PRINT ALPHABET FROM GIVEN ARGUMENT

import sys
from terre_fonctions import create_alphabet


# Part 1 : Error Handling

if not (len(sys.argv) == 2 and sys.argv[1].lower() in create_alphabet()):
    print("erreur.")
    exit()


# Part 2 : Parsing

letter = sys.argv[1].lower()
alphabet = create_alphabet()
letter_index = alphabet.index(letter)
alphabet_from_argument = "".join(alphabet[letter_index:])


# Part 3 : Display

print(alphabet_from_argument)