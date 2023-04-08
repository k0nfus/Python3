import random

schere = "✂️" # 1
stein = "🪨" # 2
papier = "📜" # 3

# intro
print("  " + schere + "      " + stein + "      " + papier)
print("Schere, Stein, Papier")
print("... ohne Brunnen!")

# inputs
human = input("1 für Schere, 2 für Stein, 3 für Papier: ")
computer = random.randint(1,3)

# control
print("Der Computer entscheidet sich für " + str(computer))
print("Du hast dich für " + str(human) + " entschieden.")

# who won?
if int(human) == int(computer):
    print("Unentschieden!")
elif int(human) == 1 and int(computer) == 2:
    print("Der Computer gewinnt mit dem " + stein)
elif int(human) == 2 and int(computer) == 3:
    print("Der Computer gewinnt mit " + papier)
elif int(human) == 3 and int(computer) == 1:
    print("Der Computer gewinnt mit "+ schere)
else:
    print("  " + schere + "    " + stein + "    " + papier)
    print("Du hast gewonnen!")
    print("  " + schere + "    " + stein + "    " + papier)