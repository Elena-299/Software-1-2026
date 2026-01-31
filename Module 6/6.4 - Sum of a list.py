def sum_of_list(list):
    sum = 0
    for i in list:
        sum = sum + i
    return sum

list = []
num = input("Enter a number or press enter to quit: ")

while num != "":
    num = int(num)
    list.append(num)
    num = input("Enter a number or press enter to quit: ")

print(sum_of_list(list))