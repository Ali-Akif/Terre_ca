import sys

if len(sys.argv) == 1:
    exit()
chaine = " ".join(sys.argv[1:])


    # méthode 1:

for i in range(len(chaine)):
    print(chaine[-i-1],end="")
print()


    # méthode 2:

print(chaine[::-1], end="")
print()


    # méthode 3:
chaine_reverse = ""
for i in range(len(chaine)-1, -1, -1):
    chaine_reverse += chaine[i]
print(chaine_reverse)


    # méthode 4:
chaine_reverse = ""
for i in range(1, len(chaine) +1):
    chaine_reverse += chaine[-i]
print(chaine_reverse)

    # méthode 5:
chaine_reverse =""
for i in chaine:
    chaine_reverse = i + chaine_reverse
print(chaine_reverse)

    # méthode 5:
print(chaine[len(chaine):-1:-1])