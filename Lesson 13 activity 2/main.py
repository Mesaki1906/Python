# Create Floyd's Triangle using loops

rows = int(input("Please enter the total number of rows: ")) # Take input
number = 1 # Initialise by 1

print("Floyd's Triangle")
for i in range(1, rows + 1): # Outer loop for number of rows
    for j in range(1, i + 1): # Inner loop for number of columns
        print(number, end = "") # Display Result
        number = number + 1
    print()
