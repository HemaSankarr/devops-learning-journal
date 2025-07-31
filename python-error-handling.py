# Importing a standard library module
import math

def divide_numbers(a, b):
    try:
        result = a / b
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Use math module safely
try:
    number = float(input("Enter a number: "))
    print(f"Square root of {number}: {math.sqrt(number)}")
except ValueError:
    print("Invalid number!")
except Exception as e:
    print(f"Unexpected error: {e}")

# Test division
divide_numbers(10, 0)  # This will cause ZeroDivisionError
divide_numbers(10, 2)  # This should succeed
