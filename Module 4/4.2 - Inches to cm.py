inches = float(input("Enter the number of inches: "))
while inches >= 0:
    inches = inches * 2.54
    print(f"That number of inches is {inches:.2f}cm.")
    inches = float(input("Enter the number of inches: "))
