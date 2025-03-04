def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def main():
    print("Welcome to the Simple Calculator!")
    print("Select the operation you want to perform:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == '1':
            print(f"The result of adding {num1} and {num2} is: {add(num1, num2)}")
        elif choice == '2':
            print(f"The result of subtracting {num2} from {num1} is: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"The result of multiplying {num1} and {num2} is: {multiply(num1, num2)}")
        elif choice == '4':
            result = divide(num1, num2)
            if result == "Error! Division by zero.":
                print(result)
            else:
                print(f"The result of dividing {num1} by {num2} is: {result}")
    else:
        print("Invalid input. Please enter a number between 1 and 4 to select an operation.")

if __name__ == "__main__":
    main()