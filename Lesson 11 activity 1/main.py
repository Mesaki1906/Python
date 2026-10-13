# Chores and Task list

total_chores = 4
original_count = total_chores
print(f"You have {original_count} chores to do today! \n")

# Counter for completed and current chores
completed_count = 0
chore_num = 1

# Repeat while there are chores left to do

while chore_num <= total_chores:

    # Work out the current chores name from its number
    if chore_num ==1: next_chore = "Make your bed"
    elif chore_num ==2: next_chore = "Feed your pet"
    elif chore_num ==3: next_chore = "Take out the trash"
    else: next_chore = "Wash dishes"

    answer = input(f"Have you finished : {next_chore}? (yes/no): ")

    # move to next chore once its marked done
    if answer == "yes":
        completed_count += 1
        chore_num += 1
        print("Great job! Chore completed")
    else:
        print("Okay, finish the chore and check again!")

    # How many chores remain after each check
    print("Chores remaining: ", total_chores - completed_count)
    print()

# Print final message after every chore is complete

print("===== ALL CHORES COMPLETED =====")
print("You have completed all your chores for today! Good job!")

# A look at what infinite loop would look like
print("Now lets take a peek at an infinite loop...")
test_value = 0
safety_counter = 0
while test_value <= 0:
    print("This condition never changes, so this loop will run forever!")
    break

# Print final chore checklist summary

print("\n===== CHORE CHECKLIST SUMMARY =====")
print("Chores assigned today: ", original_count)
print("Chores completed: ", completed_count)
print("Chores remaining: ", total_chores - completed_count)
print("====================================")
