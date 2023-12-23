import sys

if len(sys.argv[1:]) != 2:
    print("erreur.")
    exit()
else:
    a, b = sys.argv[1], sys.argv[2]


if not (a.lstrip("-+").isdigit() and b.lstrip("-+").isdigit()):
    print("erreur.")
    exit()
elif b < "1":
    print("erreur.")
    exit()

resultat = int(a) 
exposant = 0

for i in range(1, int(b)):
    resultat *= int(a)

print(resultat)
