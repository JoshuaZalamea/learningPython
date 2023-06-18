import random

# variables
trollHP = random.randint(25,50)
playerHP = 50
playerDMG = None
move = None
potions = 3

print(" ")
print("You stumble across a troll in a cave")

while playerHP > 0:
    if trollHP > 0:
        print(" ")
        move = None
        trollDMG = random.randint(5,10)
        print("--- Troll's HP:", trollHP, "---")
        print("Your HP:", playerHP, "| Potions:", potions)
        print("ATTACK | DEFEND | HEAL")
        move = input("Action: ")
        trollDMG = random.randint(5,15)
        print(" ")
        if move == "ATTACK":
            playerDMG = random.randint(5,10)
            print("YOU attack the troll with your sword, dealing", playerDMG, "damage!")
            trollHP = trollHP - playerDMG
            # end script
            print("The TROLL swings his club, dealing", trollDMG, "damage!")
            playerHP = playerHP - trollDMG
        if move == "DEFEND":
            block = random.randint(5,10)
            trollDMG = trollDMG - block
            if trollDMG <= 0:
                trollDMG = 0
                print("Perfect block!")
            else:      
                print("YOU raise your shield and block", block, "incoming damage!")
                # end script
                print("The TROLL swings his club, dealing", trollDMG, "damage!")
                playerHP = playerHP - trollDMG
        if move == "HEAL":
            if potions > 0:
                heal = random.randint(5,10)
                playerHP = playerHP + heal
                potions = potions - 1
                if playerHP >= 50:
                    print("YOU drink a health potion and heal", heal, "HP")
                    print("Your health is now full!")
                    playerHP = 50
                    # end script
                    print("The TROLL swings his club, dealing", trollDMG, "damage!")
                    playerHP = playerHP - trollDMG
                else:
                    print("YOU drink a health potion and heal", heal, "HP")
                    print("Your current HP has been raised to", playerHP)
                    # end script
                    print("The TROLL swings his club, dealing", trollDMG, "damage!")
                    playerHP = playerHP - trollDMG
            elif potions <= 0:
                print("YOU are out of potions!")
        else:
            None
    else:
        break
print(" ")
death = 2
if trollHP <= 0:
    death = death + 1
if playerHP <= 0:
    death = death - 2
else:
    print(" ")

# death options

if death == 3:
    print("Congratulations! YOU defeated the TROLL!")
if death == 0:
    print("YOU died.")
if death == 1:
    print("YOU strike eachother and fall simultaneously.")
else:
    print(" ")