# Factorial

def factorial(x):
    '''This is a recursive function to find the factorial of an integer'''

    if x==0 or x==1:
        return 1
    else:
        # Callig function inside function
        return x*factorial(x-1)

# Display Results
print(factorial.__doc__)
print("The factorial of 0: ",factorial(0))
print("The factorial of 1: ",factorial(1))
print("The factorial of 2: ",factorial(2))
print("The factorial of 5: ",factorial(5))
print("The factorial of 10: ",factorial(10))
