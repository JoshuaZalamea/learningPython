attempts = 3
name = "Josh"
guess = None

while guess != "Josh" and attempts > 0:
    print("Attempts remaining:", attempts)
    guess = (input("Guess my name: "))
    if guess == "Josh":
        print("Correct! You win!")
    else:
        attempts = attempts - 1

if guess != "Josh":
    print("You lose")
else:
    None