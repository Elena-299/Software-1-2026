import random

count = int(input("Enter the number of dice you want to roll: "))
sum = 0

for index in range(count):
    x = random.randint(1,6)
    sum = sum + x

print(f"The sum of all the dice is {sum}")
