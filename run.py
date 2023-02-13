from healthAmounts import inputHealth

x = 0
total = 0
comboCount = 0
damageScaling = 1.0
hpScaling = 1.0

opponentMaxHP = inputHealth("What is your opponent's max HP: \n")
opponentCurrentHP = inputHealth("What is your opponent's current HP: \n")


while x != "q":
    x = input("Enter the damage of the attack (press q to quit): \n")
    if (x == "q" or x == "Q"):
        break
    comboCount = comboCount + 1
    if comboCount >= 10:
        damageScaling = 0.1
    elif comboCount == 9:
        damageScaling = 0.2
    elif comboCount == 8:
        damageScaling = 0.3
    elif comboCount == 7:
        damageScaling = 0.4
    elif comboCount == 6:
        damageScaling = 0.5
    elif comboCount == 5:
        damageScaling = 0.6
    elif comboCount == 4:
        damageScaling = 0.7
    elif comboCount == 3:
        damageScaling = 0.8

    print("HP before combo ", opponentCurrentHP)
    if (opponentCurrentHP/opponentMaxHP) <= 0.15:
        hpScaling = 0.75
    elif (opponentCurrentHP/opponentMaxHP) <= 0.25:
        hpScaling = 0.90
    elif (opponentCurrentHP/opponentMaxHP) <= 0.50:
        hpScaling = 0.95

    print("Combo Count ", comboCount)
    print("Attack value", x)
    print("Total Damage before Subtraction ", total)
    total = total + (hpScaling * damageScaling * int(x))
    opponentCurrentHP = opponentCurrentHP - (hpScaling * damageScaling * int(x))
    print("Total Damage to this point ", total)
    print("HP after combo ", opponentCurrentHP)

("Thank you for playing. Final total is ", opponentCurrentHP)