from healthAmounts import healthAmount;

userCharacter = ""; 
# which character the user is playing as and wishing to check the damage for.
opponentCharacter = "";
# which character the user is doing damage to and calculating the remaining health for.
opponentStartingHealth = 0;
# global variable for the starting health of the opponent character. Will be a number between 850 and 1100.
comboCount= 0;
# increments as more attacks are performed in a row. As this variable increases, combo damage decreases.
healthCheck = 1;
# at regular points the opponent health will be checked and then multiplied by this number.
# at full health they will receive full damage (multiplied by 1), but this variable will decrease proportional to their health.
settingUp = True;
# condition intended to shut down the while loop
stillCalculating = True;
# condition intended to shut down the while loop
implementedCharacters = {"ryu", "chun-li", "deejay"};
# Unordered set containing characters currently with valid data for calculating
validOpponents = healthAmount.values;

while settingUp:
        if userCharacter.lower (input("Please enter your character name (Ryu, Deejay or Chun-Li)")) not in implementedCharacters:
                print("Please enter a valid character name");
        else: 
                print("Thank you")
                if opponentCharacter.lower ("Please enter your opponent\'s character") not in validOpponents:
                        print("Please enter a valid character name");
                else:
                        print("Thank you")
                        settingUp = False;