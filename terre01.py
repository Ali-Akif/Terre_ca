import os
import sys

#si executé depuis le terminal :

print(sys.argv[0])

#si executé autrement :

chemin = __file__
fichier = os.path.basename(chemin)
print("Nom du fichier :", fichier)