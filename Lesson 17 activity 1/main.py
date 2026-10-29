# Vending Machine

# 1. Function that works out change and sends it back with return

def calculate_change(paid, price):
    change = paid = price
    return change

# 2. Set the snack price and greet customer

snack_price = 25
print("===== SNACK VENDING MACHINE =====")
print(f"This snack costs {snack_price} units.")
print("Accepted coins: 1, 5, 10, 25\n")

total_inserted = 0
coins_inserted = 0

# 3. Keep accepting coins until enough money is inserted
while True:
    coin = int(input("Insert a coin (1, 5, 10, 25): "))

    # 4. Reject any coin that isnt valid value

    if coin != 1 and coin != 5 and coin != 10 and coin != 25:
        print("Invalid coin, try again! \n")
        continue

    # 5. Add the value coin to the running total

    total_inserted += coin
    coins_inserted += 1
    print(f"Inserted {coin}. Total so far: {total_inserted}\n")

    # 6. Stop askling for coins once enough has been inserted
    
    if total_inserted >= snack_price:
        print("Enoug money inserted! \n")
        break

# 7. Work out the change using the value returned by calculate_change

change_due = calculate_change(total_inserted, snack_price)

print("Dispensing Your snack.....")

# 8. Nothing extra to do when change is exactly 0

if change_due == 0:
    pass
else:
    print(f"Here is your change: {change_due} units")

# 9. Print a short summary of the purchase

print("\n ======= PURCHASE SUMARY =======")
print("Snack price: ", snack_price)
print("Coins inserted: ", coins_inserted)
print("Total paid: ", total_inserted)
print("Change given: ", change_due)
print("==================================")
print("Thanks for your purchase!!!")
