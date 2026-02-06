seasons = ("spring", "summer", "autumn", "winter")

print("Hello, for this program you will need to input a number that corresponds to a month \n ")
print("The numbers are 1 through 12, being the months January through December \n ")

month = int(input("Enter the number of the month: "))

if month==3 or month==4 or month==5:
    print(f"This month is in {seasons[0]}")

elif month==6 or month==7 or month==8:
    print(f"This month is in {seasons[1]}")

elif month==9 or month==10 or month==11:
    print(f"This month is in {seasons[2]}")

elif month==12 or month==1 or month==2:
    print(f"This month is in {seasons[3]}")

else:
    print("There is no month corresponding to this number")