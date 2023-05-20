name = input("Enter a username: ")
password = input("Enter a password: ")
print("To lock your computer, type lock")
command = None
input1 = None
input2 = None
while command != "lock":
    command = input("Command: ")
while input1 != name:
    input1 = input("Username: ")
while input2 != password:
    input2 = input("Password: ")
print("Login successful!")