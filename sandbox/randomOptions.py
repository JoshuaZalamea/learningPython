import random

def test1():
    print("test success")

test2 = 3

options = [test1(), test2, 'Option 3']

random_selection = random.sample(options, 3)

print("Randomized Options:")
for i, option in enumerate(random_selection, start=1):
    print(f"{i}. {option}")

user_choice = int(input("Select your option (1-3): "))

# Validate user input
while user_choice not in [1, 2, 3]:
    print("Invalid choice. Please try again.")
    user_choice = int(input("Select your option (1-3): "))

selected_option = random_selection[user_choice - 1]
print("You selected:", selected_option)