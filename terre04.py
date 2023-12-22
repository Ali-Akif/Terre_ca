import sys

arg = sys.argv[1:]

if len(arg) > 1:
    print("Rentre qu'un seul argument.")
    exit()

if not int(arg[0].lstrip("+-").isdigit()):
    print("Tu ne me la mettras pas à l'envers.")
    exit()

elif int(arg[0]) % 2 == 0:
    print("pair")

else:
    print("impair")