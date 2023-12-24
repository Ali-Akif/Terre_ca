import sys

if not (len(sys.argv) > 1 and "".join(sys.argv[1:]).isdigit()):
    print("erreur.")
    exit()
else:
    liste = sys.argv[1:]

trie = True
for i in range(len(liste) - 1):
    if not (int(liste[i]) <= int(liste[i+1])):
        trie = False

if trie:
    print("Triée !")
else:
    print("Pas triée !")