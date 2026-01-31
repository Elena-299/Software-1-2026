import random

def random_dice(side):
    dice = random.randint(1,side)
    return dice

dice = 0
dice_side = int(input("Enter the number of sides on the dice: "))

while dice != dice_side:
    dice = random_dice(dice_side)
    print(dice)
