# Unit Converter: Build a program that converts units (e.g., Celsius to Fahrenheit, kilometers to miles).

def lengthConverter():
    print("\n Length Conversion: ")
    print("1. Metres to Kilometres")
    print("2. Kilometres to Metres")
    print("3. Feet to Metres")
    print("4. Metres to Feet")

    choice = int(input("Choose a conversion option (1-4): "))
    value = float(input("Enter the value to convert: "))

    if choice == 1:
        print(f"{value} metres is equal to {value / 1000} kilometres.")
    elif choice == 2:
        print(f"{value} kilometres is equal to {value * 1000} metres.")
    elif choice == 3:
        print(f"{value} feet is equal to {value * 0.3048} metres.")
    elif choice == 4:
        print(f"{value} metres is equal to {value / 0.3048} feet.")
    else:
        print("Invalid Option")

def weightConverter():
    print("\n Weight Conversion")
    print("1. Kilograms to Grams")
    print("2. Grams to Kilograms")

    choice = int(input("Choose a conversion option (1-2): "))
    value = float(input("Enter the value to convert: "))

    if choice == 1:
        print(f"{value} kilograms is equal to {value * 1000} grams.")
    elif choice == 2:
        print(f"{value} grams is equal to {value / 1000} kilograms.")
    else:
        print("Invalid Option")

def temperatureConverter():
    print("\n Temperature Conversion")
    print("1. Celcius to Fahrenheit")
    print("2. Fahrenheit to Celcius")

    choice = int(input("Choose a conversion option(1-2): "))
    value = float(input("Enter the temperature value to convert: "))

    if choice == 1:
        converted = (value* 9/5) + 32
        print(f"{value} Celcius is equal to {converted} Fahrenheit.")
    elif choice == 2:
        converted = (value - 32) * 5/9
        print(f"{value} Fahrenheit is eqaul to {converted} Celcius")
    else:
        print("Invalid Option")

def unitConverter():
    while True:
        print("\n")
        print("\n")
        print("__________________________________________")
        print("_________    Unit Converter    ___________")
        print("__________________________________________")
        print("1. Length Conversion")
        print("2. Weight Conversion")
        print("3. Temperature Conversion")
        print("4. Exit")

        choice = int(input("Choose an option(1-4): "))

        if choice == 1:
            lengthConverter()
        elif choice == 2:
            weightConverter()
        elif choice == 3:
            temperatureConverter()
        elif choice == 4:
            print("The program is ended. Have a  nice day.")
            print("____________________________")
            print("\n")
            print("\n")
            break
        else:
            print("Invalid Option. Please choose a valid number")

unitConverter()