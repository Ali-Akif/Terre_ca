#Créez un programme qui affiche le résultat et le reste d’une division entre deux nombres.

import sys

if len(sys.argv[1:]) != 2:
    print("erreur.")
    exit()
elif not sys.argv[1].lstrip("+-").isdigit():
    print("erreur.")
    exit()
elif not sys.argv[2].lstrip("+-").isdigit():
    print("erreur.")
    exit()

a = int(sys.argv[1])
b = int(sys.argv[2])

if b > a:
    print("erreur.")
    exit()

elif b == 0:
    print("erreur.")
    exit()

else:
    print(f"""résultat: { a // b}
reste: { a % b }""")