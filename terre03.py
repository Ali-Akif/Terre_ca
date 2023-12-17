#Créez un programme qui affiche les arguments qu’il reçoit ligne par ligne, peu importe le nombre d’arguments.

import sys 

for i in sys.argv[1:]: 
    print(i)