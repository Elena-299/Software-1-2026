talent = float(input("Enter the talent: "))
pound = float(input("Enter the pound: "))
lot = float(input("Enter the lot: "))

tott_gram = (lot * 13.3) + (pound * 13.3 * 32) + (talent * 13.3 * 32 * 20)
kilos = int(tott_gram / 1000)
grams = float(tott_gram - kilos * 1000)

print(f"The weight in modern units is: {kilos} kilograms and {grams:2.5} grams.")
