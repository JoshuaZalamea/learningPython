import random

number = random.randint(1,50)
guess = -1
attempts = 0

print("Let's play guess the number!")
while guess != number:
    print(" ")
    guess = int(input("Is it..."))

    if guess == number:
        print(" ")
        print("You win!")
    elif guess < number:
        print("Too low...")
        attempts = attempts + 1
    elif guess > number:
        print("Too high...")
        attempts = attempts + 1

if attempts >= 3:
    print ("Wow, that must have been difficult.")
else:
    None