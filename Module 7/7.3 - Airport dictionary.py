print("Hello, welcome to the airport data! \n")
print("There are only 3 possible commands: \n"
      "new - to enter a new airport into the system \n"
      "search - to search for an existing airport from the system \n"
      "quit - to exit the program \n")

airports = {}
option = str(input("Please enter which command you want: "))

while option != "quit":
    if option == "new":
        name = str(input("What is the name of the airport: "))
        icao = str(input("What is the ICAO code of the airport: "))
        icao = icao.upper()
        airports[icao] = name
        option = str(input("Please enter which command you want: "))

    elif option == "search":
        icao = str(input("What is the ICAO code of the airport: "))
        icao = icao.upper()
        name = airports[icao]
        print(f"The name of the airport is {name}")
        option = str(input("Please enter which command you want: "))

    else:
        option = str(input("Invalid command, enter another one: "))

print("You have decided to exit the program\nGoodbye!")
