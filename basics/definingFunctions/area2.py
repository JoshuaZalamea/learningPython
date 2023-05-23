def hello():
    print("Hello")

def area(width, height):
    return width * height

def name_welcome(name):
    print("Welcome,", name)

def positive_input(prompt):
    number = float(input(prompt))
    while number <= 0:
        print("Must be a positive number")
        number = float(input(prompt))
    return number

def print_menu():
    print()
    print("Which shape are you measuring?")
    print(" R for rectangle")
    print(" S for square")
    print(" C for circle")
    print(" Q to quit")
    print()

choice = None

name = input("Your name: ")
hello()
name_welcome(name)

while choice != "Q":
    if choice == "R":
        print()
        print("To find the area of a rectangle,")
        print("enter the width and height below:")
        print()
        w = positive_input("Width: ")
        h = positive_input("Height: ")
        print("Width =", w, "Height =", h, "so area =", area(w, h))
        choice = None
    elif choice == "S":
        print("")
        print("To find the area of a square,")
        print("enter the length of one side below:")
        print("")
        s = positive_input("Side length: ")
        print("Side length =", s, "so area =", area(s,s))
        choice = None
    elif choice == "C":
        print("")
        print("To find the area of a circle,")
        print("enter the radius below:")
        print("")
        r = positive_input("Radius: ")
        print("Radius =", r, "so area =", 3.14 * r ** 2)
        choice = None
    else:
        print_menu()
        choice = input("Option: ")