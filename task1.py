# 1. Create the dictionary (you can edit/add students here)
students = {
    "Sita": 85,
    "Bob": 92,
    "Charlie": 78
}

# 2. Ask user for a name
name_input = input("Enter the student's name: ").strip()

# 3. Try exact match first
marks = students.get(name_input)

# 4. If not found, try case-insensitive lookup
if marks is None:
    lower_map = {k.lower(): v for k, v in students.items()}
    marks = lower_map.get(name_input.lower())

    if marks is not None:
        # find original-cased name to print prettily
        original_name = next(k for k in students if k.lower() == name_input.lower())
        print(f"{original_name}'s marks: {marks}")
    else:
        print("Student not found.")
else:
    print(f"{name_input}'s marks: {marks}")
