def addition (a, b):
    return (a + b)

def subtract (a, b):
    return (a - b)

def multiply (a, b):
    return (a * b)

def division (a, b):
    return "if number divide by zero is zero" if b == 0 or a == 0 else a/b

result = division(67, 0)
print(result)

while True:
    print("\n--- Calculator Dashboard ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == '5':
        print("Exiting...")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", addition(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", division(num1, num2))
    else:
        print("Invalid option!")