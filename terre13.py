import sys

if len(sys.argv) != 4:
    print("erreur.")
    exit()

a = "".join(sys.argv[1:])
if not a.isdigit():
    print("erreur.")
    exit()

a, b, c = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])

liste = [a, b, c]
liste_trie = []

if a < b and a < c:
    liste_trie.append(a)
    liste.remove(a)
elif b < a and b < c:
    liste_trie.append(b)
    liste.remove(b)
elif c < a and c < b:
    liste_trie.append(c)
    liste.remove(c)
else:
    print("erreur.")
    exit()

if liste[0] < liste[1]:
    liste_trie.append(liste[0])
    liste_trie.append(liste[1])
else:
    liste_trie.append(liste[1])
    liste_trie.append(liste[0])

print(liste_trie[1])

