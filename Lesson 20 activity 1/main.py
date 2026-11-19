# Python Function calculator

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print("Select your operation")
print("1. Add \n2.Subtract \n3.Multiply \n4.Divide")

choice = input("Enter your choice (1/2/3/4): ")

try:
    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))

    if choice == "1":
        print("Result: ", add(num1, num2))
    elif choice == "2":
        print("Result: ", subtract(num1, num2))
    elif choice == "3":
        print("Result: ", multiply(num1, num2))
    elif choice == "4":
        print("Result: ", divide(num1, num2))
    else:
        print("INVALID CHOICE")
except ValueError:
    print("Error, Enter valid numbers")
except ZeroDivisionError:
    print("Error, Zero can't be divided by any number")
