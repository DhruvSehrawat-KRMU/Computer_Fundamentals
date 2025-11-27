def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

def main():
    print("=== CALCULATOR ===")

    print("1. Add")
    print("2. Subtract") 
    print("3. Multiply")
    print("4. Divide")

    choice = input("Choose operation (1-4): ")

    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))

    if choice == "1":
        result = add_numbers(num1, num2)
        print(f"Result: {result}")
    elif choice == "2":
        result = subtract_numbers(num1, num2)
        print(f"Result: {result}")
    elif choice == "3":
        result = multiply_numbers(num1, num2)
        print(f"Result: {result}")
    elif choice == "4":
        result = divide_numbers(num1, num2)
        print(f"Result: {result}")
    else:
        print("Invalid choice!")

    print("Done!")

if __name__ == "__main__":
    main()

