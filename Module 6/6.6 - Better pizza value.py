import math
def unit_pizza(diameter, price):
    diameter_meters = diameter / 100
    area = diameter_meters * diameter_meters * math.pi
    unit = price / area
    return unit

diameter1 = float(input("Enter the diameter of the first pizza in centimeters: "))
price1 = float(input("Enter the price of the first pizza in euros: "))
unit1 = unit_pizza(diameter1, price1)
#print(f"{unit1:4.3}")

diameter2 = float(input("Enter the diameter of the second pizza in centimeters: "))
price2 = float(input("Enter the price of the second pizza in euros: "))
unit2 = unit_pizza(diameter2, price2)
#print(f"{unit2:4.3}")

if unit1 > unit2:
    print("The second pizza provides better value for its price.")
else:
    print("The first pizza provides better value for its price.")