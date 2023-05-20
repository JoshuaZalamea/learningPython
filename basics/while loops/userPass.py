username = input("Username: ")
password = input("Password: ")
userPass = username+password
lock = "N"
a = "n"
b = "n"
c = "n"

while lock != "Y":
    lock = input("Lock? Y/N: ")

while c != userPass:
    a = input("Username: ")
    b = input("Password: ")
    c = a + b

print("You're in!")