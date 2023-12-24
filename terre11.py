import sys

if len(sys.argv) != 2:
    print("Merci de ne rentrer qu'un seul argument.")
    exit()
else:
    arg = sys.argv[1]

if not (len(arg) == 5 and arg.replace(":", "").isdigit() and arg.count(":") == 1 and arg.index(":") == 2):
    print("Merci de rentrer une heure au format HH:MM")
    exit()
else:
    arg = arg.split(":")


if int(arg[0]) > 23:
    print("Merci de rentrer une heure valide.")
    exit()
elif int(arg[1]) > 59:
    print("Merci de rentrer une heure valide.")
    exit()
else:
    h = int(arg[0])
    min = arg[1]

if h > 12:
    a = "PM"
else:
    a = "AM"

if h == 0:
    h = 12

if a == "PM":
    h -= 12

print(f"{h}:{min}{a}")




