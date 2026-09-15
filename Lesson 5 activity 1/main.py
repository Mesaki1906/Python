# Ask for temperature
temperature = int(input("Enter today's temperature in celsius: "))

# Decide betwwen shirt or jacket
if temperature < 20:
    outfit = "jacket"
    print("It is cold today.")
    print("Wear a", outfit)
else:
    outfit = "t-shirt"
    print("It is a warm day.")
    print("Wear a", outfit)

# Ask if its raining
is_raining = input("Is it raining today? (yes/no): ")

# Decide if an umbrella is needed
if is_raining == "yes":
    print("Bring an umbrella!")

# Ask for windspeed
wind_speed = int(input("Enter the wind speed in km/h: "))

# Decide if a windbreaker is needed
if wind_speed > 30:
    neeeds_windbreaker = "yes"
    print("It is windy today.")
    print("Wear a windbreaker over your", outfit)
else:
    needs_windbreaker = "no"
    print("it is calm today.")
    print("No windbreaker needed over your", outfit)

# Ask weather there are puddles
are_puddles = input("Are there puddles on the gound? (yes/no): ")

# Decide if boots are needed
if are_puddles == "yes":
    shoes = "boots"
    print("the ground is wet.")
    print("Wear", shoes, "today.")
else:
    shoes = "sneakers"
    print("the ground is dry.")
    print("Wear", shoes, "today.")

# Weather check complete
print("")
print("Weather check completed")

# Print final summary of outfit
print("Weather Outfit picker")
print("Temperature", temperature)
print("Outfit:", outfit)
print("Raining:", is_raining)
print("Windbreaker needed:", needs_windbreaker)
print("Shoes chosen:", shoes)
