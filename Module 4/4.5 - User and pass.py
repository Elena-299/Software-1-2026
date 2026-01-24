username = str(input("enter the username: "))
password = str(input("Enter the password: "))
count = 1
while count < 5:
    if (username == "python") and ( password == "rules"):
        print("Welcome")
        break
    else:
        print("Enter username and password again")
        username = str(input("Enter username: "))
        password = str(input("Enter password: "))
        count = count + 1
    if count == 5:
        print("Access denied")
        break
