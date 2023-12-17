#Créez un programme qui affiche l’alphabet à partir de la lettre donnée en argument en lettres minuscules suivi d’un retour à la ligne.

import sys

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

if sys.argv > 1 and sys.argv < 3:
    argument_terminal = sys.argv[1]

argument_terminal = argument_terminal.index(argument_terminal)

print(alphabet[argument_terminal:])
