num = str(input("Enter a number, or press enter to quit: "))
order = []

while num != "":
    num = int(num)
    order.append(num)
    num = str(input("Enter a number, or press enter to quit: "))

order.sort(reverse = True)
print(order)

for i in range(0,5):
    print(order[i])
