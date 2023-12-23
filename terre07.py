import sys

if sys.argv[2:]:
    print("erreur.")
    exit()
else:
    chaine = sys.argv[1]
    nb = 0

if chaine.isdigit():
    print("erreur.")
    exit()
else:
    for i in chaine:
        nb += 1
print(nb)