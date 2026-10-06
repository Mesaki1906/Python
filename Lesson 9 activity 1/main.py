# Car Picker (Nested if else statements)

print("=== WELCOME TO RIDE BUILDER ===" "\n")

print("STEP 1 = Pick Your Vehicle")
print("1. Bike")
print("2. Car" "\n")

choice = int(input("Enter 1 or 2: "))

if choice == 1:

    # Nested if else statement
    print("STEP 2 = Pick your bike type")
    print("1. Scooter")
    print("2. Mountain Bike" "\n")

    bike_type = int(input("Enter 1 or 2: "))
    print()

    if bike_type == 1:
        print("Your choice : Scooter")
        print("Top Speed   : 80 km/h")
        print("Best for    : City Commute")
    else:
        print("Your choice : Mountain Bike")
        print("Top Speed   : 40 km/h")
        print("Best for    : Off-road trail")

elif choice == 2:

    # Nested if else statement, runs only if 2nd option is true
    print("STEP 2 = Pick your car type")
    print("1. Sedan")
    print("2. SUV" "\n")

    car_type = int(input("Enter 1 or 2: "))
    print()

    if car_type == 1:
        print("Your choice : Sedan")
        print("Seats       : 5")
        print("Top Speed   : 160 km/h")
        print("Best for    : Family Adventure")

    else:
        print("Your choice : SUV")
        print("Seats       : 7")
        print("Top Speed   : 180 km/h")
        print("Best for    : Off-road Adventure")

else:
    print("INVALID INPUT")
    print("Enter 1 for bike or 2 for car")

print()
print("=== THANK YOU FOR USING RIDE BUILDER ===")
