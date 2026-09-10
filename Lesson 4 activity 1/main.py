# Farm Yeild Calculator

field1 = 120
field2 = 85
field3 = 150
field4 = 95
field5 = 110

# Calculating total and average
total = field1 + field2 + field3 + field4 + field5
average = total / 5

print("Total harvest :", total, "KG")
print("Average per field : ", average, "KG")

# Price per KG
price_per_kg = 15
earnings = total * price_per_kg
print("Total earnings: ", earnings, "RS")

# Floor division and Modulus
bags = total // 25
leftover = total % 25

print("Full bags packed :", bags)
print("Leftover harvest :", leftover, "KG")

# Compare Yeilds with last year
last_year = 500
print("Better than last year? :", total > last_year)
print("Same as last year? :", total == last_year)
print("Atleast as good? :", total >= last_year)

# Bonus Field add 30KG
total += 30
print("After Bonus crop :", total, "KG")

# Subtract 15KG for seeds
total -= 15
print("After seeds reserve :", total, "KG")

# Final bags
bags = total // 25
print("Final bags packed :", bags)
