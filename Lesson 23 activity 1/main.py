# Dictionary of students (id -> details)

student_data = {
    "id1": {"name": "Sara", "class": "V", "subject_integration": "english, math, science"},
    "id2": {"name": "David", "class": "V", "subject_integration": "english, math, science"},
    "id3": {"name": "Sara", "class": "V", "subject_integration": "english, math, science"},
    "id4": {"name": "Surya", "class": "V", "subject_integration": "english, math, science"},
}

result = {}
seen_keys = [] # Using a list instead of set

for student_id, details in student_data.items():
    unique_keys = (details["name"], details["class"],
details["subject_integration"])

    if unique_keys not in seen_keys:
        seen_keys.append(unique_keys)
        result[student_id] = details

# Print output line by line

for k, v in result.items():
    print(k, ":", v)
