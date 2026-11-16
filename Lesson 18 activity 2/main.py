# Try with else and finally

try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print("Result is", result)
except ZeroDivisionError:
    print("Division by zero is error!!!")
except ValueError:
    print("Please enter a valid whole number!")
except:
    print("Wrong Input!")
else:
    print("No exceptions")
finally:
    print("This will execute no matter what")
