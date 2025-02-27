import math
import sys

def square_root(x):
    return math.sqrt(x)

def factorial(x):
    return math.factorial(x)

def natural_log(x):
    if x <= 0:
        raise ValueError("Natural log is only defined for positive numbers.")
    return math.log(x)

def power(x, b):
    return math.pow(x, b)

def main():
    if len(sys.argv) > 1:
        # Handle command-line arguments for Docker execution
        choice = sys.argv[1]
        if choice == "1" and len(sys.argv) == 3:
            print(f"Result: {square_root(float(sys.argv[2]))}")
        elif choice == "2" and len(sys.argv) == 3:
            print(f"Result: {factorial(int(sys.argv[2]))}")
        elif choice == "3" and len(sys.argv) == 3:
            print(f"Result: {natural_log(float(sys.argv[2]))}")
        elif choice == "4" and len(sys.argv) == 4:
            print(f"Result: {power(float(sys.argv[2]), float(sys.argv[3]))}")
        else:
            print("Invalid command-line arguments.")
        return

    # Interactive mode (for normal execution)
    print("\nScientific Calculator")
    operations = {
        "1": ("Square Root", lambda x: square_root(float(x))),
        "2": ("Factorial", lambda x: factorial(int(x))),
        "3": ("Natural Logarithm", lambda x: natural_log(float(x))),
        "4": ("Power Function", lambda x, y: power(float(x), float(y)))
    }

    while True:
        print("\n1. Square Root")
        print("2. Factorial")
        print("3. Natural Logarithm")
        print("4. Power Function")
        print("5. Exit")

        choice = input("Choose an operation (1-5): ")
        if choice in operations:
            try:
                if choice == "4":
                    x = input("Enter base: ")
                    y = input("Enter exponent: ")
                    print(f"Result: {operations[choice][1](x, y)}")
                else:
                    x = input("Enter number: ")
                    print(f"Result: {operations[choice][1](x)}")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

