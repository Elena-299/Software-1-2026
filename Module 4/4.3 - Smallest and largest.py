num = str(input("Enter a number: "))
max = min = float(num)
while num != "":
    num = float(num)
    if num > max:
        max = num
        num = str(input("Enter a number: "))
    elif num < min:
        min = num
        num = str(input("Enter a number: "))
    num = str(input("Enter a number: "))
print(f"The largest number given was {max}, and the smallest was {min}")
