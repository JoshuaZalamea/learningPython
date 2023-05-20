import random

number = random.randint(1,50)
guess = -1

print("Let's play guess the number!")
while guess != number:
    guess = int(input("Is it..."))

    if guess == number:
        print("You win!")
    elif guess < number:
        print("Too low...")
    elif guess > number:
        print("Too high...")