def read_temperature() -> float:
    """Read temperature from user input."""
    while True:
        try:
            temperature = float(input("Enter temperature to convert: "))
            return temperature
        except ValueError:
            print("Invalid input. Please enter a valid temperature.")


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32


def select_conversion() -> int:
    """Select the conversion type from user input."""
    valid_choices = [1, 2, 3]
    print("\nChoose your desired conversion:")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")
    print("3. Exit")
    
    while True:
        try:
            direction = int(input("Choose your desired conversion: "))
            if direction not in valid_choices:
                print("Invalid input. Please enter a valid choice.")
            else:
                return direction
        except ValueError:
            print("Invalid input. Please enter a valid choice.")


def main():
    """Run the temperature converter application."""
    print("Welcome to Temperature Converter")
    
    while True:
        selection = select_conversion()
        
        match selection:
            case 1:
                print("\nSelected: Fahrenheit to Celsius")
                unit_from = "°F"
                unit_to = "°C"
                temperature = read_temperature()
                result = fahrenheit_to_celsius(temperature)
            case 2:
                print("\nSelected: Celsius to Fahrenheit")
                unit_from = "°C"
                unit_to = "°F"
                temperature = read_temperature()
                result = celsius_to_fahrenheit(temperature)
            case 3:
                print("Goodbye!")
                break
        
        print(f"Result: {temperature:.2f} degrees {unit_from} = "
              f"{result:.2f} degrees {unit_to}")
        
        another_version = input(
            "Do you want to convert another temperature? "
            "Enter 'n' to exit. Any other key for yes: "
        )
        
        if another_version.lower() == "n":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()