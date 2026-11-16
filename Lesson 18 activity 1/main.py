# Using a Try and Except:

try:
    number = int(input("Enter a number: "))
    print("The number entered is: ", number)

# Using Value error
except ValueError as ex:
    print("Exception: ", ex)
