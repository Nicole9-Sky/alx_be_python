FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9  
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5  

def convert_to_celsius(fahrenheit):

    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius  


def convert_to_fahrenheit(celsius):

    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit 

def main():
    print("Welcome to the Temperature Conversion Tool!") 

    try:
        temp = float(input("Enter the temperature you want to convert: "))
        
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        if unit == 'F':
            converted = convert_to_celsius(temp) 
            print(f"{temp}°F is {converted:.2f}°C") 

        elif unit == 'C':
            converted = convert_to_fahrenheit(temp) 
            print(f"{temp}°C is {converted:.2f}°F")  

        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
