# Right angle triangle using the loop function of python

print("Half Pyramid Pattern of Stars (*):")
n= int(input("enter the number of rows: ")) # Take input
for i in range(n): # Outer loop handling number or rows
    for j in range(i+1): # Inner loop handling number of columns
        print("*", end="") # Display result
    print()
