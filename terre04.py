#Créez un programme qui affiche l’alphabet à partir de la lettre donnée en argument en lettres minuscules suivi d’un retour à la ligne.

import sys

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

if len(sys.argv) > 1 and len(sys.argv) < 3:

    for arg in range(1, len(sys.argv)):
        argt_terminal = sys.argv[1]

    if argt_terminal in alphabet:
        index = alphabet.index(argt_terminal)
        print("".join(alphabet[index :]))

    else:
        print("L'argument n'est pas dans l'alphabet")

else:
    print("y'a erreur la frérot")
