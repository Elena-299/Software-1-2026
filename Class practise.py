# TUESDAY 20.2.2026
# money = float(input("Enter amount of money: "))
# print("You can buy a latte.")
# if money>=5:
#     pass
#
#
# cat = input("Enter the name of the cat: ")
# dog = input("Enter the name of the dog: ")
# if cat==dog:
#     print("Oh my! The cat and dog have the same name!")
#
#
# Medicine
# # age = int(input("Enter the age of the patient: "))
# # if 15 <= age < 18:
# #     weight = float(input("Enter the patients weight: "))
# # if age >= 18 or age >= 15 and weight > 55:
# #     print("The medicine can be administered")
# #     print("The medicine cannot be administered")
#
# # ELEIF statement
# # age = int(input("Enter your age: "))
# # if age >= 65:
# #     print("You are retired, unc!")
# # elif age >= 20:
# #     print("You are of working age.")
# # elif age >= 7:
# #     print("You are a student")
# # else:
# #     print("You are a child")
#
#
# # Module 3 ex1
# # age = int(input("Enter your age: "))
# # if age >= 18:
# #     print("You are old enough to vote in the Finnish parlamentary elections")
# # else:
# #     remainder = 18 - age
# #     print(f"You can vote in {remainder} years")
#
#
# #Module 3 ex2
# # kWh = float(input("What is your electricity consumtion: "))
# # if kWh <= 50:
# #     bill = kWh * 0.10
# # elif kWh <= 200:
# #     bill = (50 * 0.10) + ((kWh - 50) * 0.08)
# # else:
# #     bill = (50 * 0.10) + (150 * 0.08) + ((kWh - 200) * 0.06)
# # print(f"Your bill is ${bill:.2f}")
#
#
# #Module 3 ex3
# physics = int(input("Enter your physics result: "))
# math = int(input("Enter your math result: "))
# chemistry = int(input("Enter your chemistry result: "))
#
# if (physics or math or chemistry) < 50:
#     print("You can not get the scholarship")
# elif ((physics and math) > 90) or chemistry > 95:
#     print("You can get the scholarship, congrats!")
# else:
#     print("You can not get the scholarship")


#               THURSDAY 22.2.2026
#   expl1
# rounds = int(input("Enter the number of rounds: "))
# finished = 0
# while finished < rounds:
#     print("Good morning!")
#     finished = finished + 1

# command = input("Enter a command: ")
# command = command.lower()
# while command != "stop":
#     print("Executing command : ", command)
#     command = input("Enter a command: ")
# print("Execution stopped.")

#       example:
# password = ""
# while password != "Python123":
#     password = str(input("Enter Password: "))
#     print("Incorrect Password, try again")
# print("Correct Password")
#

# import random
# count = 0
# tottal = 0
# while count <= 100000:
#     dice1 = dice2 = rolls = 0
#     while dice1 != 6 or dice2 != 6:
#         dice1 = random.randint(1, 6)
#         dice2 = random.randint(1, 6)
#         rolls += 1
#     tottal = tottal + rolls
#     #print(rolls)
#     count += 1
# print(int(tottal/count))
# print("end sequence.")


#             Nested loop
# count = 1
# while count <= 100000:
#     outer = 1
#     while outer <= 5:
#         inner = 1
#         while inner <= 5:
#             print(f"Loop {count} - {outer} times {inner} is {outer * inner}")
#             inner += 1
#         outer += 1
#     count += 1
# print("Code finished")

#       While with else
# command = input("Enter a command: ")
# while command != "stop":
#     if command == "MAYDAY":
#         break
#     print(f"Executing command: {command}")
#     command = input("Enter a command: ")
# else:
#     print("Goodbye")
# print("Code finalised.")

#26.2.2026

#NOTES:
#when adding random library
#inser random.uniform(L,U), to get a random float
# but with limits
#


#27.1.2026.
# names = []
# names = ["apples", "oranges", "banana", "watermelon"]
# print(name)
# print(names[0])
# print(names[-1])
# print(names[1:3])
# print(len(names))

# names = []
# name = input("Enter the first name or quit by pressing enter: ")
# while name != "":
#     names.append(name)
#     name = input("Enter the next name or  quit by pressing enter: ")
# print(names)
#
# for n in names:
#     print(f"Hello, {n}")

# for n in range(5, 0, -1):
#     print(x)


# Mod5 ex set:
#1
# num = int(input("Enter a number: "))
# if num <= 0:
#     print("Invalid number. Error!")
# else:
#     for i in range(0, num+1, 2):
#         print(i)

#2
# numbers = []
# num = str(input("Enter a number, or press enter if you want to quit: "))
# while num != "":
#     num = int(num)
#     numbers.append(num)
#     num = str(input("Enter another number, or press enter if you want to quit: "))
# print(numbers)
#
# temp = []
# for i in numbers:
#     if i > 100:  #and not in temp
#         if i not in temp:
#             temp.append(i)
# for n in temp:
#     print(n)


# # 29.1.2026
# def beautiful_day()#(parameter):            #keyword name():
#     print("Wow this is a sunny day today.")
#     return
#
# beautiful_day()                 #call is without any keywords


# def sum_of_numbers(a,b):
#     sum = a + b
#     return sum
#
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
#
# print(x)
# x = sum_of_numbers(num1, num2)

# #expl:
# def change():
#     city = "Vantaa"         #local variable {city}
#     print(f"The city is {city}")
#     return
#
# city = "Helsinki"           #global variable {city}
#
# print(f"The city in the beginning of the program is {city}")
# change()
# print(f"The city at the end of the program is {city}")

# area pf rectangle, circle and change of temp C to F
# # #ex1
# def area_rectangle(a,b):
#     area = a * b
#     return area
#
# length = float(input("Enter the length of the rectangle: "))
# width = float(input("Enter the width of the rectangle: "))
# area = area_rectangle(length, width)
# print(f"The area of this rectangle is {area}")
#
# #ex2
# import math
# def area_circle(r):
#     pi = math.pi
#     area_c = r * r * pi
#     return area_c
#
# radius = float(input("Enter the circle radius: "))
# area_c = area_circle(radius)
# print(area_c)
#
# #ex3
# def temperature_switch(temp):
#     farenheit = (temp * 9/5) + 32
#     return farenheit
# celcious = float(input("Enter the the temperature in celsious: "))
#
# print(temperature_switch(celcious))

# def greet(greeting, times):
#     for i in range(times)
#         print(greeting + "round" + str(i+1))
#     return
# print("This is and example of loop")
# times = int(input("Enter times: "))
# greeting = input("Enter a greeting: ")
#greet(greeting, times)

# def greeting(times, greet):
#     for i in range(times):
#         print(greet)
#     return
# greet = str(input("Enter a greeting, or done to end: "))
# count = int(input("Enter the number of iteration: "))
# while greet != "done":
#     greeting(count, greet)
#     greet = str(input("Enter a greeting, or done to end: "))
#     count = int(input("Enter the number of iteration: "))
# print("code done")

# def inventory(items):
#     print("You have the following item:")
#     for item in items:
#         print(item)
#     return
#
# backpack = ["laptop", "book", "notepad", "charger"]
# inventory(backpack)

#4.1.2026
#Touple - tough     ()
#
# days_of_week = ("Monday", "Tuesday", ...)
#
# fruits = "orange", "banana", "apple"
#
# # (first, second, third) = fruits
# import random
#
# def cast():
#     first, second = random.randint(1, 6), random.randint(1,6)
#     return first, second
#
# dice1, dice2 = cast()
# print(f"The dice show {dice1} and {dice2}")


#SET - specific {}
#
# list = []
# touple = ()
# set = set()
#
# games = {"Monopoly", "Chess", "Cluedo"}
# print(games)
#
# games.add("Dominion")
# games.remove("Chess")
# games.add("Monopoly")
#
# print(games)


#DICTIONARY - dual  {key:value}
#
# num = {"Viivi": "050-1234567",
#        "Ahmed": "040-1112223",
#        "Olga": "050-1011012"}
#
# name = input("Enter name: ")
# print(num)
# if name in num:
#     print(f"{name}'s phone is {num[name]}.")

#examples:
#num1:
# fruit = {}
# for i in range(3):
#     name = input("Enter the name of the fruit: ")
#     weight = float(input("Enter the weight of the fruit in kg: "))
#     fruit[name] = weight
# print(fruit)

# #num2:
# num = int(input("Enter a number: "))
# list = []
# unique = set()
#
# while num != 0:
#     list.append(num)
#     num = int(input("Enter a number: "))
#
# new_set = set(list)
#
# for i in list:
#     unique.add(i)
#
# print(unique)
# print(new_set)

#num3:
#NEW FAV
# question = str(input("Enter 'new' / 'search' / 'quit' :  "))
# phonebook = {}
#
# while question != "quit":
#     if question == "new":
#         name = str(input("Enter the persons name: "))
#         phone_number = str(input("Enter their phone number: "))
#         phonebook[name] = phone_number
#         question = str(input("Enter 'new' / 'search' / 'quit' :  "))
#
#     elif question == "search":
#         name = str(input("Enter the persons name: "))
#         if name in phonebook:
#             print(phonebook[name])
#         else:
#             print("Name not found try again.")
#
#     else:
#         print("Command not recognise, try again!")
#
#     question = str(input("Enter 'new' / 'search' / 'quit' :  "))
#
# print(phonebook)

# 4.2.2026
#
# import mariadb
# print(mariadb.__version__)
#
# connection = mariadb.connect(host="127.0.0.1",
#                              port=3306,
#                              user="root",
#                              password="Python",
#                              database="people",
#                              autocommit=True)
# print("Connection established.")
#
# def get_first_name(connection, first_name):
#     sql = "SELECT * FROM people WHERE first_name = ?"
#     cursor = connection.cursor()
#     cursor.execute(sql, (first_name,))
#     result = cursor.fetchall()
#     if result:
#         for a in result:
#             print(f"{a[0]} is {a[1]}")


# 10.2.2026.






















