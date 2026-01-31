def gallon_to_litre(gallon):
    litre = gallon * 3.78541
    return litre

US_gallon = float(input("Enter the amount of gallons, or enter a negative number to quit: "))
while US_gallon >= 0:
    SI_litre = gallon_to_litre(US_gallon)
    print(f"That amount in litres is {SI_litre:5.2f}")
    US_gallon = float(input("Enter the amount of gallons, or enter a negative number to quit: "))

