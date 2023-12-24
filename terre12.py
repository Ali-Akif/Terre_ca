import sys

if len(sys.argv) != 2:
    print("Merci de rentrer un seul argument.")
    exit()
else:
    arg = sys.argv[1]

arg = arg.zfill(7)


if not( len(arg) == 7 and arg.replace(":", "").replace("PM", "").replace("AM","").isdigit() and arg.count(":") == 1 and arg.index(":") == 2 ):
    print("Merci de rentrer une heure en format : 12:30PM.")
    exit()
elif not arg.index("M") == 6:
    print("Merci de de rentrer une heure au bon format, comme 12:30AM.")
    exit()

liste = arg[:-2].split(":") + [arg[-2:]]

h, m, a = int(liste[0]), int(liste[1]), liste[2]

if not ( 1<= h <13 and m <60 ):
    print("C'est pas une heure ça frérot")
    exit()

if a == "PM":
    if a != 12:
        h += 12
elif a == "AM" and h == 12:
    h -= 12


print(f"{'0' if h < 10 else ''}{h}:{m}")

