
def calculator():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operator = input("Choose an operation (+, -, *, /): ").strip()

            if operator not in ['+', '-', '*', '/']:
                print("Invalid operation! Please choose from +, -, *, or /.")
                continue

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    print("Division by zero is not allowed.")
                    continue
                result = num1 / num2

            print(f"Result: {result}")

        except ValueError:
            print("Invalid input! Please enter numeric values only.")
            continue

        again = input("Would you like to perform another calculation? (yes/no): ").strip().lower()
        if again != 'yes':
            break

if __name__ == "__main__":
    calculator()
