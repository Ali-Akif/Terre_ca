import sys

if len(sys.argv) != 2:
    print("Merci de ne rentrer qu'un seul argument.")
    exit()


if not sys.argv[1].lstrip("+").isdigit():
    print("Merci de rentrer un chiffre.")
    exit()

else:
    nb = int(sys.argv[1])
compteur = 0
for i in range(1, nb+1):
    if nb % i == 0:
        compteur +=1
    
if compteur == 2:
    print(f"Oui, {nb} est un nombre premier.")
else:
    print(f"Non, {nb} n'est pas un nombre premier.")