cabin = str(input("Enter your cruise cabin class: "))
cabin = cabin.upper()
if cabin == "LUX":
    print("You have an upper-deck cabin with a balcony.")
elif cabin == "A":
    print("You have an above the car deck cabin, equipped with a window.")
elif cabin == "B":
    print("You have a windowless cabin above the car deck.")
elif cabin == "C":
    print("You have a windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")
