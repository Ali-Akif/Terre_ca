import sys

if len(sys.argv) != 2:
    print("erreur.")
    exit()
else:
    arg = sys.argv[1]

if not arg.isdigit():
    print("erreur.")
    exit()


resultat = int(arg) **0.5
print(resultat)