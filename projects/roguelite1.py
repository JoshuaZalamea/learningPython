import random

def sp():
    print(" ")

# enemy encounters
def dr_fight():
    sp()
    sp()

# shop
def shop():
    sp()
    print("You round a corner and find a shopkeep with lushious")
    print("blonde hair standing behind a table stocked with wares")
    sp()
    print("ONE TACO: Hello! I'm One Taco, back from dead to rip you off!")
    sp()

def item1():
    print("item1")

def item2():
    print("item2")

def item3():
    print("item3")

def item4():
    print("item4")

def item5():
    print("item5")

def item6():
    print("item6")

items = [item1(), item2(), item3(), item4(), item5(), item6()]
random.shuffle(items)
print(items)

# test area
shop()