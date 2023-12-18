#Créez un programme qui affiche l’alphabet à partir de la lettre donnée en argument en lettres minuscules suivi d’un retour à la ligne.

import sys

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

if len(sys.argv) == 2:
    
    for arg in sys.argv[1]:
        arg = arg.lower()
        if arg in alphabet:
            index = alphabet.index(arg)
            print("".join(alphabet[index:]))
        else:
            print(" pas dans alphabet")
else:
    print("rentre une lettre de l'alphabet en argument frère")


    
