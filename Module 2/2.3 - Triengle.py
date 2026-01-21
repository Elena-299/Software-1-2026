length = float(input("Enter the length of the triangle: "))
width = float(input("Enter the width of the triangle: "))
hypotenuse = float((length * length + width * width) ** 0.5)

area = 0.5 * length * width
print(f"The area of the triangle is: {area}")

perimeter = hypotenuse + length + width
print(f"The perimeter of the triangle is: {perimeter}")