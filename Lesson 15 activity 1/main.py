# Lemonade Stand Calculator

# 1. Define function with no arguments

def greet_customer():
    print("Welcome to the lemonade stand!!")
    print("Fresh Lemonade, made just for you.")

# 2. Call function

greet_customer()

# 3. Ask for the price per cup and number of cups sold

price_per_cup = float(input("Enter the price per cup in Dollars: "))
cups_sold = int(input("Enter the number of cups sold: "))

# 4. Define function that takes arguments and returs the total cost

def calculate_total(price, cups):
    total = price * cups
    return total

# 5. Call calculate_total and store value it returns

total_cost = calculate_total(price_per_cup, cups_sold)

# 6. Use built-in function to round the total and then print it

rounded_total = round(total_cost, 2)
print("Total Cost: ", rounded_total)

# 7. Ask how much money the customer paid

amount_paid = float(input("Enter the amount paid by the customer: "))

# 8. Define a function that takes arguments and returns the change due

def calculate_change(paid, total):
    change = paid - total
    return change

# 9. Call calculate_change and store the value it returns

change_due = calculate_change(amount_paid, rounded_total)
rounded_change = round(change_due, 2)

# 10. Define a function that returns a thank you message based on the amount of cups sold

def thank_you_message(cups):
    if cups >= 5:
        return "Wow, big order! Thank you for your suport!"
    else:
        return "Thanks for stopping by the stand!"

# 11. Call thank_you_message and store the value it returns

closing_message = thank_you_message(cups_sold)

# 12. Print the final lemonade stand recipt
print("\n ===== LEMONADE STAND RECIPT =====")
print("Price per cup: ", price_per_cup)
print("Cups Sold: ", cups_sold)
print("Total cost: ", rounded_total)
print("Amount Paid: ", amount_paid)
print("Change Due: ", rounded_change)
print(closing_message)
print("========================================")
