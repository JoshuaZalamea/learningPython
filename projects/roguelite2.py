import random

player_name = input("What is your name, crewmember? ")
player_hp = 20
player_dmg = 10
player_agility = 10
player_crit = 0

def combat(enemy_name, enemy_hp, enemy_dmg):
    global player_hp, player_dmg, player_dodge, player_name
    print("A", enemy_name, "blocks your path forward.")
    print(" ")
    while enemy_hp > 0:
        precision_shot = 0
        spray_pray = 0
        dodge = 0
        print(enemy_name)
        print("<3 " * (enemy_hp // 4))
        print("")
        print(player_name)
        print("<3 " * (player_hp // 4))
        print("")
        print("What action will you take?")
        print("1. Precision shot")
        print("2. Spray and pray")
        print("3. Dodge")
        choice = input("Selection: ")
        while choice != '1' and choice != '2' and choice != '3':
            if choice == '1':
                print("test")
                

def level_up():
    global player_hp, player_dmg, player_agility
    print("You leveled up! Choose an attribute to increase.")
    print("1. Health", '[', player_hp, ']')
    print("2. Damage", '[', player_dmg, ']')
    print("3. Agility", '[', player_agility, ']')
    print("4. Crit")
    choice = input("Selection: ")
    while choice != '1' and choice != '2' and choice != '3':
        if choice == '1':
            player_hp = player_hp + random.randint(5,10)
        elif choice == '2':
            player_dmg = player_dmg + random.randint(3,6)
        elif choice == '3':
            player_agility = player_agility + random.randint(1,3)
        else:
            print("Invalid input.")
            choice = input("Selection: ")

level_up()
combat("Toad", 30, 20)
level_up()