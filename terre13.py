# FIND THE MIDDLE VALUE

import sys
from terre_fonctions import EH_argument_lenght_and_is_digit


# Part 1 : Function

def valeur_du_milieu(a,b,c):
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

    return liste_trie[1]


# Part 2 : Error Handling

EH_argument_lenght_and_is_digit(sys.argv[1:], 3)


# Part 3 : Parcing and Resolution


a, b, c = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])

resultat = valeur_du_milieu(a,b,c)



# Part 3 : Display

print(resultat)


