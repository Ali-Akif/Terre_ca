#Créez un programme qui affiche les arguments qu’il reçoit ligne par ligne, peu importe le nombre d’arguments.

import sys

arg = sys.argv[1:]
for i in arg:
    print(i)