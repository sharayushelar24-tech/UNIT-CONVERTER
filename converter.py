# UNIT CONVERTER - FULL PYTHON PROJECT

def length_converter():
    print("\n--- LENGTH CONVERTER ---")
    print("1. Kilometer to Meter")
    print("2. Meter to Kilometer")
    print("3. Centimeter to Meter")
    print("4. Meter to Centimeter")

    choice = int(input("Enter your choice: "))
    value = float(input("Enter value: "))

    if choice == 1:
        print("Result:", value * 1000, "meters")
    elif choice == 2:
        print("Result:", value / 1000, "kilometers")
    elif choice == 3:
        print("Result:", value / 100, "meters")
    elif choice == 4:
        print("Result:", value * 100, "centimeters")
    else:
        print("Invalid choice!")


def weight_converter():
    print("\n--- WEIGHT CONVERTER ---")
    print("1. Kilogram to Gram")
    print("2. Gram to Kilogram")
    print("3. Kilogram to Pound")
    print("4. Pound to Kilogram")

    choice = int(input("Enter your choice: "))
    value = float(input("Enter value: "))

    if choice == 1:
        print("Result:", value * 1000, "grams")
    elif choice == 2:
        print("Result:", value / 1000, "kilograms")
    elif choice == 3:
        print("Result:", value * 2.20462, "pounds")
    elif choice == 4:
        print("Result:", value / 2.20462, "kilograms")
    else:
        print("Invalid choice!")


def temperature_converter():
    print("\n--- TEMPERATURE CONVERTER ---")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = int(input("Enter your choice: "))
    value = float(input("Enter value: "))

    if choice == 1:
        print("Result:", (value * 9/5) + 32, "°F")
    elif choice == 2:
        print("Result:", (value - 32) * 5/9, "°C")
    else:
        print("Invalid choice!")


def time_converter():
    print("\n--- TIME CONVERTER ---")
    print("1. Hours to Minutes")
    print("2. Minutes to Hours")
    print("3. Seconds to Minutes")
    print("4. Minutes to Seconds")

    choice = int(input("Enter your choice: "))
    value = float(input("Enter value: "))

    if choice == 1:
        print("Result:", value * 60, "minutes")
    elif choice == 2:
        print("Result:", value / 60, "hours")
    elif choice == 3:
        print("Result:", value / 60, "minutes")
    elif choice == 4:
        print("Result:", value * 60, "seconds")
    else:
        print("Invalid choice!")


def main():
    while True:
        print("\n=========== UNIT CONVERTER ===========")
        print("1. Length Converter")
        print("2. Weight Converter")
        print("3. Temperature Converter")
        print("4. Time Converter")
        print("5. Exit")

        ch = int(input("Enter your choice: "))

        if ch == 1:
            length_converter()
        elif ch == 2:
            weight_converter()
        elif ch == 3:
            temperature_converter()
        elif ch == 4:
            time_converter()
        elif ch == 5:
            print("Thank you for using the Unit Converter!")
            break
        else:
            print("Invalid choice! Please try again.")

main()
