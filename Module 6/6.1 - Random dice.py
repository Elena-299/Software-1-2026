import random

def random_dice():
    dice = random.randint(1,6)
    return dice

dice = 0
while dice != 6:
    dice = random_dice()
    print(dice)
