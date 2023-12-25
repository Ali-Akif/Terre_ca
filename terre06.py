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
print(chaine[len(chaine):-1:-1])