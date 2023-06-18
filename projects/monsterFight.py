import random

bossHealth = 50
attempt = 0
success = 0

print("You enter the mouth of a gloomy cave,")
print("The claws and teeth of a demon you brave,")
print("With breath as foul as a river stagnant,")
print("Your sword held high you charge in, gallant!")

while bossHealth > 0:
    random_integer = random.randint(1, 3)
    attack = int(input("Attack: "))
    if attack == random_integer:
        bossHealth = bossHealth - 5
        success = success + 1
    attempt = attempt + 1
    print("Boss health:",bossHealth)

print("The terrible creature wails loudly,")
print("Over vicera and guts you step, proudly.")
print("----------------------------------------")
print("Congratulations, you won!")
print("Accuracy: ", round(success/attempt*100,0),"%")