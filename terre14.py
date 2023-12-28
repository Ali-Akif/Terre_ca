# LIST ORDERED OR NOT

import sys
from terre_fonctions import EH_argument_lenght_and_is_digit


# Part 1 : Error Handling

if not (len(sys.argv) != 1 and "".join(sys.argv[1:]).isdigit()):
    "error."
    exit()


# Part 2 : Parcing
    
liste = sys.argv[1:]
trie = True


# Part 3 : Resolution

for i in range(len(liste) - 1):
    if not (int(liste[i]) <= int(liste[i+1])):
        trie = False


# Part 4 : Display 
        
if trie:
    print("Triée !")
else:
    print("Pas triée !")
