#Créez un programme qui permet de déterminer si l’argument donné est un entier pair ou impair..

import sys

if len(sys.argv) <= 2:

    for i in sys.argv[1:]:
        try:
            nb = int(i) 
            if nb % 2 == 0:
                print("pair")
            elif nb % 2 != 0:
                print("impair")

        except ValueError:
            print("tu ne me la mettras pas à l'envers...")
            sys.exit(1)


else:
    print("Tu ne me la mettras pas à l'envers...")