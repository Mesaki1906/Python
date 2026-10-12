# Reverse Order

# Input number greater than 1
n = int(input("Enter a number greater than 1: "))

# Print numbers n to 1
print("numbers from {0} to {1} are: ".format(n, 1))

# Loop to print numbers
for i in range (n,0,-1):
    print(i)
