names = set()

name = str(input("Enter a name or press enter to quit: "))

while name != "":
    if name in names:
        print("Already existing name")
        name = str(input("Enter a name or press enter to quit: "))
    else:
        names.add(name)
        print("New name")
        name = str(input("Enter a name or press enter to quit: "))

for i in names:
    print(i)
