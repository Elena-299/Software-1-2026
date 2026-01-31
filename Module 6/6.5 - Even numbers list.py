def even_numbers(full_list):
    new_list = []
    for i in full_list:
        if i % 2 == 0:
            new_list.append(i)
    return new_list

list1 = []
num = input("Enter a number, or press enter to end: ")

while num != "":
    num = int(num)
    list1.append(num)
    num = input("Enter a number, or press enter to end: ")

print(list1)
print(even_numbers(list1))
