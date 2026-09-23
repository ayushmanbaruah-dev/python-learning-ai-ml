# ============================================================
# 10_python_dictionaries.py
# Python Dictionaries
#
# Description:
# Complete practice file covering Python Dictionaries:
# - Creating dictionaries
# - Accessing dictionary items
# - Changing dictionary items
# - Adding items
# - Removing items
# - Dictionary methods
# - Looping through dictionaries
# - Nested dictionaries
# - Practical examples
#
# ============================================================


# ============================================================
# 1. CREATING A DICTIONARY
# ============================================================

# A dictionary stores data in KEY : VALUE pairs.

student = {
    "name": "Aayushman",
    "age": 22,
    "course": "Data Science",
    "marks": 85
}

print("Student:", student)


# Example:

person = {
    "name": "Rahul",
    "age": 23,
    "city": "Kolkata"
}

print("Person:", person)


# ============================================================
# 2. DICTIONARY ITEMS
# ============================================================

# Each item contains:
#
# key : value

student = {
    "name": "Aayushman",
    "age": 22,
    "marks": 85
}

print("Name:", student["name"])
print("Age:", student["age"])
print("Marks:", student["marks"])


# ============================================================
# 3. DUPLICATE KEYS
# ============================================================

# Dictionary keys must be unique.
#
# If the same key is used more than once,
# the latest value replaces the previous value.

student = {
    "name": "Aayushman",
    "age": 22,
    "age": 23
}

print("Student:", student)


# ============================================================
# 4. DICTIONARY LENGTH
# ============================================================

student = {
    "name": "Aayushman",
    "age": 22,
    "marks": 85
}

print("Number of items:", len(student))


# ============================================================
# 5. CHECK DICTIONARY TYPE
# ============================================================

print("Type:", type(student))


# ============================================================
# 6. ACCESSING DICTIONARY ITEMS
# ============================================================

student = {
    "name": "Aayushman",
    "age": 22,
    "course": "Data Science"
}

# Access using square brackets.

print("Name:", student["name"])

print("Course:", student["course"])


# ============================================================
# 7. ACCESS USING get()
# ============================================================

# get() is useful when the key might not exist.

student = {
    "name": "Aayushman",
    "age": 22
}

print(student.get("name"))

print(student.get("age"))

# If the key does not exist, get() returns None.

print(student.get("email"))


# You can also provide a default value.

print(student.get("email", "Email not available"))


# ============================================================
# 8. GET ALL KEYS
# ============================================================

student = {
    "name": "Aayushman",
    "age": 22,
    "course": "Data Science"
}

keys = student.keys()

print("Keys:", keys)


# ============================================================
# 9. GET ALL VALUES
# ============================================================

values = student.values()

print("Values:", values)


# ============================================================
# 10. GET ALL ITEMS
# ============================================================

items = student.items()

print("Items:", items)


# ============================================================
# 11. CHECK IF A KEY EXISTS
# ============================================================

student = {
    "name": "Aayushman",
    "age": 22,
    "course": "Data Science"
}

if "name" in student:
    print("Name key exists.")

if "email" not in student:
    print("Email key does not exist.")


# ============================================================
# 12. CHANGING DICTIONARY VALUES
# ============================================================

student = {
    "name": "Aayushman",
    "age": 22,
    "marks": 85
}

student["marks"] = 92

print("Updated student:", student)


# Change multiple values using update()

student.update({
    "age": 23,
    "marks": 95
})

print("After update():", student)


# ============================================================
# 13. ADDING NEW ITEMS
# ============================================================

student = {
    "name": "Aayushman",
    "age": 22
}

student["course"] = "Data Science"

print("After adding course:", student)

student["city"] = "Kolkata"

print("After adding city:", student)


# ============================================================
# 14. ADD USING update()
# ============================================================

student = {
    "name": "Aayushman",
    "age": 22
}

student.update({
    "course": "Data Science",
    "marks": 90
})

print("Updated student:", student)


# ============================================================
# 15. REMOVING ITEMS
# ============================================================

student = {
    "name": "Aayushman",
    "age": 22,
    "course": "Data Science",
    "marks": 90
}


# pop()
# Removes a specific key and returns its value.

removed_value = student.pop("marks")

print("Removed value:", removed_value)
print("After pop():", student)


# ============================================================
# 16. popitem()
# ============================================================

student = {
    "name": "Aayushman",
    "age": 22,
    "course": "Data Science"
}

removed_item = student.popitem()

print("Removed item:", removed_item)
print("After popitem():", student)


# ============================================================
# 17. del
# ============================================================

student = {
    "name": "Aayushman",
    "age": 22,
    "course": "Data Science"
}

del student["age"]

print("After del:", student)


# You can also delete the entire dictionary:

student = {
    "name": "Aayushman",
    "age": 22
}

del student

# The dictionary no longer exists.


# ============================================================
# 18. clear()
# ============================================================

student = {
    "name": "Aayushman",
    "age": 22
}

student.clear()

print("After clear():", student)


# ============================================================
# 19. COPYING A DICTIONARY
# ============================================================

student = {
    "name": "Aayushman",
    "age": 22,
    "marks": 90
}

# copy()

student_copy = student.copy()

print("Original:", student)
print("Copy:", student_copy)


# Using dict()

student_copy_2 = dict(student)

print("Second copy:", student_copy_2)


# IMPORTANT:
#
# Do not confuse:
#
# student_copy = student
#
# with:
#
# student_copy = student.copy()
#
# The first creates another reference to the same dictionary.
# The second creates a separate dictionary.


# ============================================================
# 20. LOOP THROUGH DICTIONARY
# ============================================================

student = {
    "name": "Aayushman",
    "age": 22,
    "marks": 90
}

# Loop through keys.

for key in student:
    print("Key:", key)


# ============================================================
# 21. LOOP THROUGH VALUES
# ============================================================

for value in student.values():
    print("Value:", value)


# ============================================================
# 22. LOOP THROUGH KEYS
# ============================================================

for key in student.keys():
    print("Key:", key)


# ============================================================
# 23. LOOP THROUGH KEY-VALUE PAIRS
# ============================================================

for key, value in student.items():
    print(key, ":", value)


# ============================================================
# 24. NESTED DICTIONARIES
# ============================================================

# A dictionary can contain other dictionaries.

students = {
    "student1": {
        "name": "Aayushman",
        "age": 22,
        "marks": 90
    },

    "student2": {
        "name": "Rahul",
        "age": 23,
        "marks": 85
    }
}

print("Students:", students)


# Access nested dictionary

print("Student 1:", students["student1"])

print("Student 1 name:", students["student1"]["name"])

print("Student 1 marks:", students["student1"]["marks"])


# ============================================================
# 25. MULTIPLE STUDENTS
# ============================================================

students = {
    "student1": {
        "name": "Aayushman",
        "marks": 90
    },

    "student2": {
        "name": "Rahul",
        "marks": 85
    },

    "student3": {
        "name": "Amit",
        "marks": 78
    }
}

for student_id, student_data in students.items():
    print(student_id)
    print(student_data)


# ============================================================
# 26. DICTIONARY WITH LIST
# ============================================================

student = {
    "name": "Aayushman",
    "skills": [
        "Python",
        "SQL",
        "Machine Learning"
    ]
}

print("Student:", student)

print("Skills:", student["skills"])

print("First skill:", student["skills"][0])


# ============================================================
# 27. LIST OF DICTIONARIES
# ============================================================

students = [
    {
        "name": "Aayushman",
        "marks": 90
    },

    {
        "name": "Rahul",
        "marks": 85
    },

    {
        "name": "Amit",
        "marks": 78
    }
]

print("First student:", students[0])

print("First student's name:", students[0]["name"])

print("First student's marks:", students[0]["marks"])


# Loop through list of dictionaries

for student in students:
    print(
        student["name"],
        student["marks"]
    )


# ============================================================
# 28. PRACTICAL EXAMPLE - STUDENT RECORD
# ============================================================

student = {
    "name": "Aayushman",
    "python": 85,
    "sql": 90,
    "math": 88
}

total_marks = (
    student["python"]
    + student["sql"]
    + student["math"]
)

average_marks = total_marks / 3

print("Student:", student["name"])
print("Total:", total_marks)
print("Average:", average_marks)


# ============================================================
# 29. PRACTICAL EXAMPLE - EXPENSE TRACKER
# ============================================================

expenses = {
    "food": 500,
    "transport": 300,
    "shopping": 1000,
    "internet": 700
}

total_expenses = sum(expenses.values())

print("Expenses:", expenses)
print("Total expenses:", total_expenses)


# ============================================================
# 30. PRACTICAL EXAMPLE - INVENTORY
# ============================================================

inventory = {
    "laptop": 10,
    "mouse": 50,
    "keyboard": 30,
    "monitor": 15
}

print("Inventory:", inventory)

inventory["mouse"] = 45

inventory["headphones"] = 20

print("Updated inventory:", inventory)


# ============================================================
# 31. PRACTICAL EXAMPLE - USER PROFILE
# ============================================================

user = {
    "username": "aayushman",
    "email": "user@example.com",
    "skills": ["Python", "SQL", "Pandas"],
    "experience": 0
}

print("Username:", user["username"])
print("Email:", user["email"])
print("Skills:", user["skills"])
print("Experience:", user["experience"])


# ============================================================
# 32. DICTIONARY METHODS
# ============================================================

"""
Python Dictionary Methods:

clear()
    Removes all items.

copy()
    Returns a copy of the dictionary.

fromkeys()
    Creates a dictionary from specified keys.

get()
    Returns the value of a specified key.

items()
    Returns all key-value pairs.

keys()
    Returns all keys.

pop()
    Removes a specified key.

popitem()
    Removes the last inserted key-value pair.

setdefault()
    Returns a value for a key and inserts it
    if the key does not exist.

update()
    Updates the dictionary with new key-value pairs.

values()
    Returns all values.
"""


# ============================================================
# 33. fromkeys()
# ============================================================

keys = ["name", "age", "course"]

student = dict.fromkeys(keys)

print("Dictionary:", student)


# Give all keys the same default value.

student = dict.fromkeys(keys, "Not Provided")

print("Dictionary with default values:", student)


# ============================================================
# 34. setdefault()
# ============================================================

student = {
    "name": "Aayushman",
    "age": 22
}

# Existing key

student.setdefault("name", "Unknown")

print("Existing key:", student)


# Missing key

student.setdefault("city", "Kolkata")

print("After adding missing key:", student)


# ============================================================
# 35. DICTIONARY COMPREHENSION
# ============================================================

# Dictionary comprehension is a concise way to create
# dictionaries.

numbers = [1, 2, 3, 4, 5]

squares = {
    number: number ** 2
    for number in numbers
}

print("Squares:", squares)


# With a condition

even_squares = {
    number: number ** 2
    for number in numbers
    if number % 2 == 0
}

print("Even squares:", even_squares)


# ============================================================
# 36. PRACTICAL DATA PROCESSING EXAMPLE
# ============================================================

students = [
    {"name": "Aayushman", "marks": 90},
    {"name": "Rahul", "marks": 35},
    {"name": "Amit", "marks": 78},
    {"name": "Priya", "marks": 92}
]

for student in students:

    if student["marks"] >= 40:
        result = "PASS"
    else:
        result = "FAIL"

    print(
        student["name"],
        "-",
        student["marks"],
        "-",
        result
    )


# ============================================================
# 37. CONVERTING TWO LISTS INTO A DICTIONARY
# ============================================================

names = ["Aayushman", "Rahul", "Amit"]

marks = [90, 85, 78]

student_marks = dict(zip(names, marks))

print("Student marks:", student_marks)


# ============================================================
# KEY TAKEAWAYS
# ============================================================

# 1. A dictionary stores data as KEY : VALUE pairs.
#
# 2. Example:
#
#       student = {
#           "name": "Aayushman",
#           "age": 22
#       }
#
# 3. Dictionary keys must be unique.
#
# 4. Dictionaries are changeable (mutable).
#
# 5. Access values using:
#
#       student["name"]
#
# 6. Use get() when a key may not exist:
#
#       student.get("email")
#
# 7. keys() returns all keys.
#
# 8. values() returns all values.
#
# 9. items() returns key-value pairs.
#
# 10. Use "in" to check whether a key exists.
#
# 11. Change a value:
#
#       student["marks"] = 95
#
# 12. Add a new item:
#
#       student["city"] = "Kolkata"
#
# 13. update() can add or modify multiple items.
#
# 14. pop() removes a specific key.
#
# 15. popitem() removes the last inserted key-value pair.
#
# 16. del removes a specific key or the entire dictionary.
#
# 17. clear() removes all items.
#
# 18. copy() creates a separate dictionary copy.
#
# 19. Dictionaries can contain:
#     - Lists
#     - Tuples
#     - Other dictionaries
#     - Numbers
#     - Strings
#     - Boolean values
#
# 20. Nested dictionaries are useful for structured data.
#
# 21. A list of dictionaries is extremely common in
#     real-world Python applications and APIs.
#
# 22. Dictionary comprehension provides a concise way
#     to create dictionaries.
#
# 23. Dictionaries are especially important for:
#     - JSON
#     - APIs
#     - Web development
#     - Data processing
#     - Automation
#     - Configuration
#     - Machine learning pipelines
#
# 24. IMPORTANT:
#
#     LIST
#         [value1, value2, value3]
#
#     TUPLE
#         (value1, value2, value3)
#
#     SET
#         {value1, value2, value3}
#
#     DICTIONARY
#         {"key": value}
#
# ============================================================