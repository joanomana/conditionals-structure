print("Exercise 7")
print()
print("This program is a basic calculator")
print()
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

def calculator():
    print("1. Addition = +")
    print("2. Subtraction = -")
    print("3. Multiplication = *")
    print("4. Division = /")
    print("5. elevation = **")
    print("6. Exit = 6")
    choice = str(input("Enter the operation number: "))
    if choice == "+":
        print("The result is: ", num1 + num2)
    elif choice == "-":
        print("The result is: ", num1 - num2)
    elif choice == "*":
        print("The result is: ", num1 * num2)
    elif choice == "/":
        print("The result is: ", num1 / num2)
    elif choice == "**":
        print("The result is: ", num1 ** num2)
    elif choice == "6":
        print("Goodbye!")
    else:
        print("Invalid choice")
calculator()