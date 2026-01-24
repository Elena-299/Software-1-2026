import random
num = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))

while guess != num:
    if num < guess:
        print("Too high!")
    elif num > guess:
        print("Too low!")
    guess = int(input("Guess another number: "))
print("You have guessed the right number!")
