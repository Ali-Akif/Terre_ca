import sys
from terre_fonctions import EH_argument_lenght, hours24_to_12
# Verif qu'il n'y a qu'un seul argument, verif que la longueur correspond a 00:00, verif que y'a que des chiffres sans :, verif que : est bien placé et qu'il n'y en a qu'un seul

EH_argument_lenght(sys.argv[1:], 1)

arg = sys.argv[1]

hours24_to_12(arg)


