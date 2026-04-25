def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def modulus(a, b):
    if b == 0:
        return "Error: Modulus by zero is not allowed."
    return a % b

def power(a, b):
    return a ** b


def calculator():
    print("===== Simple Calculator =====")
    print("Operations:")
    print("  1. Addition       (+)")
    print("  2. Subtraction    (-)")
    print("  3. Multiplication (*)")
    print("  4. Division       (/)")
    print("  5. Modulus        (%)")
    print("  6. Power          (^)")
    print("  7. Exit")
    print("=============================\n")

    while True:
        try:
            num1 = float(input("Enter the first number : "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.\n")
            continue

        print("\nChoose an operation:")
        print("  1. Addition (+)")
        print("  2. Subtraction (-)")
        print("  3. Multiplication (*)")
        print("  4. Division (/)")
        print("  5. Modulus (%)")
        print("  6. Power (^)")
        print("  7. Exit")

        choice = input("\nEnter your choice (1-7): ").strip()

        if choice == '1':
            result = add(num1, num2)
            op_symbol = '+'
        elif choice == '2':
            result = subtract(num1, num2)
            op_symbol = '-'
        elif choice == '3':
            result = multiply(num1, num2)
            op_symbol = '*'
        elif choice == '4':
            result = divide(num1, num2)
            op_symbol = '/'
        elif choice == '5':
            result = modulus(num1, num2)
            op_symbol = '%'
        elif choice == '6':
            result = power(num1, num2)
            op_symbol = '^'
        elif choice == '7':
            print("Exiting calculator. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option (1-7).\n")
            continue

        if isinstance(result, str):
            print(f"\nResult: {result}")
        else:
            print(f"\nResult: {num1} {op_symbol} {num2} = {result}")

        print("\n" + "-" * 30 + "\n")
        again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if again not in ('yes', 'y'):
            print("Exiting calculator. Goodbye!")
            break
        print()


if __name__ == "__main__":
    calculator()