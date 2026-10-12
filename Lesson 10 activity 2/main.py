# Reverse a string

# Input a sentence
string = input("Enter your own string: ")

string2 = ("")

# Loop for printing in reverse
for i in string:
    string2 = i +string2

print("\nThe original string = ", string)
print("The reversed string =  ", string2)
