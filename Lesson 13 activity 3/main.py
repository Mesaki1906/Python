# Diamond shape using loops

# Take input from user
rowSize = int(input("Enter the number of rows: "))
if rowSize%2==0: # Conditions
    halfDiamRow = int(rowSize/2)
else:
    halfDiamRow = int(rowSize/2)+1
space = halfDiamRow-1

# Loop for upper portion of Diamond
for i in range(1, halfDiamRow+1): # Loops for rows
    for j in range(1, space+1): # Loop for columns
        print(end=" ")
    space = space-1
    num = 1
    for j in range(2*i-1):
        print(end=str(num))
     # Incrementing number at each column
        num = num+1
    print()
space = 1

# Loop for lower part
for i in range(1, halfDiamRow): # Loop for rows
    for j in range(1, space+1): # Loop for columns
        print(end=" ")
    space = space+1
    num = 1
    for j in range(1, 2*(halfDiamRow-i)): # Loop to print and display numbers
        print(end=str(num)) # Display result
    # Incrementing number at each column
        num = num+1
    print()
