#Créez un programme qui affiche l’alphabet à partir de la lettre donnée en argument en lettres minuscules suivi d’un retour à la ligne.

import sys

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


    
if len(sys.argv) == 2:
    for i in sys.argv[1:]:
        if i in alphabet:
            i = i.lower()
            index = alphabet.index(i)
            print("".join(alphabet[index:]))
        else:
            print("Pas dans l'alphabet")
else:
    print("Rentre une lettre de l'alphabet dans le terminal")