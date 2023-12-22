import sys

arg = sys.argv[1].lower()

if len(arg) > 1:
    print("Rentre qu'une seule lettre.")
    exit()

for a in range(ord(arg), ord("z")):
    print(chr(a), end="")

