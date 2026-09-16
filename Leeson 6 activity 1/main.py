# Smart school day planner
print("==SMART SCHOOL DAY PLANNER==")
print("Answer the following questions and I will plan your day \n")

day = input ("What day is it? (Monday to Sunday): ").strip().capitalize()
weather = input("What is the weather like? (sunny / rainy / cloudy): ").strip().lower()
homework = input("Is your homework done? (yes / no): ").strip().lower()

print()
print(f"You plan for {day}")
print("-" * 35)

# classify the day
if day in ("Friday", "Saturday"):
    print("It's the weekend, enjoy your free time!")
elif day == "Sunday":
    print("First day of the week, pack your weekly planner.")
elif day == "Thursday":
    print("It's Thursday, time to prepare for the weekend.")
elif day in ("Monday", "Tuesday", "Wednesday"):
    print("Regular School day, Stay focused")
else:
    print("Day not recognized, check the spelling!")

# And operator, Rainy or cloudy

if weather == "sunny" and homework == "yes":
    print("After school; Head to the park, great weather and homwork is done")

# OR operator, rainy or cloudy
if weather == "rainy" or weather == "cloudy":
    print("Weather tip: Pack your umbrella, it might rain today")

# NOT operator, homework not done
if not (homework == "yes"):
    print("Home work isnt done yet, do t before going out")

# Combining And and Or and Not together
if weather == "rainy" and not (homework == "yes"):
    print("Best plan : Stay in, finish homework, then relax")
elif weather == "sunny" and homework == "yes" and not (day in ("Friday", "Saturday")):
    print("Best plan : All set for school, have a nice day")
elif day in ("Friday", "Saturday") and weather == "sunny":
    print("Best plan : Good Weather for the weekend, go out and have fun")
else:
    print("Best plan : Take it one step at a time, you got it!")

print()
print("Plan complete, have a good day!")
