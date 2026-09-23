# ============================================================
#                  PYTHON BASIC — FINAL TOPIC
#                    CONTROL FLOW & LOOPS
# ============================================================
#
# Python Basic
# |
# +-- Conditions
# |   |
# |   +-- if
# |   +-- elif
# |   +-- else
# |   +-- Logical Conditions
# |   +-- Nested Conditions
# |
# +-- Match
# |   |
# |   +-- match
# |   +-- case
# |   +-- default case (_)
# |
# +-- Loops
#     |
#     +-- for loop
#     |   +-- range()
#     |   +-- break
#     |   +-- continue
#     |   +-- else
#     |
#     +-- while loop
#         +-- break
#         +-- continue
#         +-- else
#
# ============================================================
# THIS IS THE LAST MAJOR TOPIC IN THIS BASIC PYTHON COURSE.
#
# The goal of this file is not just to learn syntax.
# The goal is to understand how Python MAKES DECISIONS
# and REPEATS TASKS.
#
# After this file:
#
#       Python Basics
#            ↓
#       Python Practice / Mini Projects
#            ↓
#       NumPy
#            ↓
#       Pandas
#            ↓
#       Data Analysis
#            ↓
#       SQL
#            ↓
#       Machine Learning
#            ↓
#       AI / Generative AI / LLM Engineering
# ============================================================


# ============================================================
# 1. CONDITIONS — if
# ============================================================

# Conditions allow Python to make decisions.

age = 22

if age >= 18:
    print("You are an adult.")


# Basic structure:
#
# if condition:
#     code to execute


# Example

temperature = 35

if temperature > 30:
    print("It is a hot day.")


# ============================================================
# 2. if + else
# ============================================================

age = 17

if age >= 18:
    print("You can vote.")
else:
    print("You cannot vote yet.")


# Structure:
#
# if condition:
#     code when True
# else:
#     code when False


# ============================================================
# 3. if + elif + else
# ============================================================

marks = 82

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "F"

print("Grade:", grade)


# Python checks conditions from TOP to BOTTOM.
# The first True condition is executed.


# ============================================================
# 4. Multiple Conditions
# ============================================================

age = 25
has_id = True

if age >= 18 and has_id:
    print("Entry allowed.")
else:
    print("Entry denied.")


# ============================================================
# 5. Logical Operators in Conditions
# ============================================================

# AND
# Both conditions must be True.

age = 22
student = True

if age >= 18 and student:
    print("Adult student.")


# OR
# At least one condition must be True.

day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("Weekend.")


# NOT
# Reverses True/False.

logged_in = False

if not logged_in:
    print("Please log in.")


# ============================================================
# 6. Comparison Operators in Conditions
# ============================================================

x = 10

if x == 10:
    print("x is 10")

if x != 5:
    print("x is not 5")

if x > 5:
    print("x is greater than 5")

if x < 20:
    print("x is less than 20")

if x >= 10:
    print("x is greater than or equal to 10")

if x <= 10:
    print("x is less than or equal to 10")


# ============================================================
# 7. Membership Conditions
# ============================================================

skills = ["Python", "SQL", "Machine Learning"]

if "Python" in skills:
    print("Python is in the skill list.")

if "Java" not in skills:
    print("Java is not in the skill list.")


# ============================================================
# 8. Nested if
# ============================================================

age = 22
has_id = True

if age >= 18:

    if has_id:
        print("You can enter.")
    else:
        print("ID required.")

else:
    print("You must be 18 or older.")


# Nested conditions mean:
#
# if
#   └── if
#        └── another condition


# ============================================================
# 9. Practical Student Grade Decision
# ============================================================

student_name = "Aayushman"
marks = 85

if marks >= 90:
    grade = "A+"
    message = "Excellent performance!"

elif marks >= 80:
    grade = "A"
    message = "Very good performance."

elif marks >= 70:
    grade = "B"
    message = "Good performance."

elif marks >= 60:
    grade = "C"
    message = "Keep improving."

elif marks >= 40:
    grade = "D"
    message = "You passed."

else:
    grade = "F"
    message = "You failed."

print("Student:", student_name)
print("Marks:", marks)
print("Grade:", grade)
print("Message:", message)


# ============================================================
# 10. Python match
# ============================================================

# match is useful when you want to compare one value
# against multiple possible cases.

day = 3

match day:

    case 1:
        print("Monday")

    case 2:
        print("Tuesday")

    case 3:
        print("Wednesday")

    case 4:
        print("Thursday")

    case 5:
        print("Friday")

    case 6:
        print("Saturday")

    case 7:
        print("Sunday")

    case _:
        print("Invalid day")


# "_" works as the default case.


# ============================================================
# 11. match with Strings
# ============================================================

command = "start"

match command:

    case "start":
        print("Application started.")

    case "stop":
        print("Application stopped.")

    case "restart":
        print("Application restarted.")

    case _:
        print("Unknown command.")


# ============================================================
# 12. When to use if/elif vs match
# ============================================================

# Use if/elif when you are checking CONDITIONS.

score = 85

if score >= 90:
    print("Excellent")
elif score >= 80:
    print("Very Good")
else:
    print("Keep improving")


# Use match when you are matching a VALUE against
# specific possible cases.

status = "pending"

match status:

    case "pending":
        print("Waiting")

    case "approved":
        print("Approved")

    case "rejected":
        print("Rejected")

    case _:
        print("Unknown status")


# ============================================================
# 13. LOOPS
# ============================================================

# Loops allow us to repeat code.

# There are two major loops in Python:
#
# 1. for loop
# 2. while loop


# ============================================================
# 14. FOR LOOP
# ============================================================

# A for loop is commonly used when you want to iterate
# through a collection of values.

languages = ["Python", "SQL", "JavaScript"]

for language in languages:
    print(language)


# Output:
# Python
# SQL
# JavaScript


# ============================================================
# 15. for Loop with Strings
# ============================================================

name = "Aayushman"

for character in name:
    print(character)


# ============================================================
# 16. for Loop with Lists
# ============================================================

marks = [85, 78, 92, 88]

for mark in marks:
    print(mark)


# ============================================================
# 17. for Loop with range()
# ============================================================

# range() generates a sequence of numbers.

for number in range(5):
    print(number)


# Output:
# 0
# 1
# 2
# 3
# 4


# range(start, stop)

for number in range(1, 6):
    print(number)


# Output:
# 1
# 2
# 3
# 4
# 5


# range(start, stop, step)

for number in range(0, 11, 2):
    print(number)


# Output:
# 0
# 2
# 4
# 6
# 8
# 10


# ============================================================
# 18. for Loop + if
# ============================================================

numbers = [1, 2, 3, 4, 5, 6]

for number in numbers:

    if number % 2 == 0:
        print(number, "is even")


# ============================================================
# 19. for Loop with enumerate()
# ============================================================

skills = ["Python", "SQL", "Pandas"]

for index, skill in enumerate(skills):
    print(index, skill)


# enumerate() is useful when you need:
#
# index + value


# ============================================================
# 20. break
# ============================================================

# break immediately stops the loop.

for number in range(1, 11):

    if number == 5:
        break

    print(number)


# Output:
# 1
# 2
# 3
# 4


# ============================================================
# 21. continue
# ============================================================

# continue skips the current iteration
# and moves to the next iteration.

for number in range(1, 6):

    if number == 3:
        continue

    print(number)


# Output:
# 1
# 2
# 4
# 5


# ============================================================
# 22. for Loop with else
# ============================================================

for number in range(5):
    print(number)
else:
    print("Loop completed.")


# The else runs when the loop finishes normally.


# ============================================================
# 23. while LOOP
# ============================================================

# A while loop continues running while a condition is True.

count = 1

while count <= 5:
    print(count)
    count += 1


# Important:
#
# Always make sure the condition eventually becomes False.
#
# Otherwise you may create an INFINITE LOOP.


# ============================================================
# 24. Practical while Loop
# ============================================================

balance = 100

while balance > 0:

    print("Current balance:", balance)

    balance -= 20


print("Balance finished.")


# ============================================================
# 25. while + if
# ============================================================

number = 1

while number <= 10:

    if number % 2 == 0:
        print(number, "is even")

    number += 1


# ============================================================
# 26. while + break
# ============================================================

number = 1

while number <= 10:

    if number == 5:
        break

    print(number)

    number += 1


# ============================================================
# 27. while + continue
# ============================================================

number = 0

while number < 5:

    number += 1

    if number == 3:
        continue

    print(number)


# ============================================================
# 28. while + else
# ============================================================

number = 1

while number <= 5:

    print(number)

    number += 1

else:
    print("While loop completed.")


# ============================================================
# 29. for vs while
# ============================================================

# FOR LOOP
#
# Use when you are iterating over:
# - list
# - tuple
# - set
# - dictionary
# - string
# - range
# - other iterable objects
#
# Example:

for item in ["Python", "SQL", "Pandas"]:
    print(item)


# WHILE LOOP
#
# Use when repetition depends on a CONDITION.
#
# Example:

count = 1

while count <= 3:
    print(count)
    count += 1


# Easy way to remember:
#
# FOR
# "For every item, do this."
#
# WHILE
# "While this condition is True, keep doing this."


# ============================================================
# 30. NESTED LOOPS
# ============================================================

# A loop inside another loop.

for row in range(3):

    for column in range(3):

        print("Row:", row, "Column:", column)


# Nested loops are useful for:
# - tables
# - matrices
# - grids
# - combinations
# - comparing multiple datasets


# ============================================================
# 31. Practical Student Marks Processing
# ============================================================

students = [
    {"name": "Aayushman", "marks": 85},
    {"name": "Rahul", "marks": 72},
    {"name": "Amit", "marks": 91},
    {"name": "Priya", "marks": 64}
]

for student in students:

    name = student["name"]
    marks = student["marks"]

    if marks >= 90:
        grade = "A+"

    elif marks >= 80:
        grade = "A"

    elif marks >= 70:
        grade = "B"

    elif marks >= 60:
        grade = "C"

    else:
        grade = "F"

    print(name, "-", marks, "-", grade)


# ============================================================
# 32. Practical Number Search
# ============================================================

numbers = [10, 25, 37, 42, 55, 68]

target = 42

for number in numbers:

    if number == target:
        print("Target found:", target)
        break


# ============================================================
# 33. Practical Expense Processing
# ============================================================

expenses = [500, 250, 1200, 300, 750]

total = 0

for expense in expenses:
    total += expense

print("Total expenses:", total)


# ============================================================
# 34. Simple Menu using while + match
# ============================================================

# This combines the concepts learned in this file.

running = True

while running:

    print("\n1. Start")
    print("2. Help")
    print("3. Exit")

    choice = input("Choose an option: ")

    match choice:

        case "1":
            print("Program started.")

        case "2":
            print("This is the help section.")

        case "3":
            print("Goodbye!")
            running = False

        case _:
            print("Invalid option.")


# ============================================================
# 35. MINI PROJECT — NUMBER GUESSING GAME
# ============================================================

# This combines:
# - variables
# - input()
# - int()
# - while loop
# - if / elif / else
# - break
# - comparison operators


secret_number = 7

print("\nNumber Guessing Game")
print("Guess a number between 1 and 10.")

while True:

    guess = int(input("Enter your guess: "))

    if guess == secret_number:

        print("Correct! You guessed the number.")
        break

    elif guess < secret_number:

        print("Too low. Try again.")

    else:

        print("Too high. Try again.")


# ============================================================
# 36. HOW PROFESSIONAL PROGRAMMERS THINK ABOUT CONTROL FLOW
# ============================================================

# Before writing code, ask:
#
# 1. Do I need to MAKE A DECISION?
#       ↓
#    Use if / elif / else
#
# 2. Am I checking ONE VALUE against many fixed options?
#       ↓
#    Consider match
#
# 3. Do I need to REPEAT something for every item?
#       ↓
#    Use for
#
# 4. Do I need to repeat something while a condition is True?
#       ↓
#    Use while
#
# 5. Do I need to stop a loop early?
#       ↓
#    Use break
#
# 6. Do I want to skip one iteration?
#       ↓
#    Use continue
#
# 7. Do I need to perform something after a loop finishes normally?
#       ↓
#    Use else with the loop


# ============================================================
# 37. IMPORTANT MENTAL MODEL
# ============================================================

# Python programs generally follow this flow:
#
#
#                  START
#                    |
#                    v
#                INPUT DATA
#                    |
#                    v
#              MAKE A DECISION
#              /             \
#           TRUE             FALSE
#            |                 |
#            v                 v
#         ACTION            OTHER ACTION
#            \                 /
#             \               /
#              v             v
#                 REPEAT?
#                    |
#              +-----+-----+
#              |           |
#             YES          NO
#              |           |
#              v           v
#             LOOP        OUTPUT
#                          |
#                          v
#                         END
#
#
# This mental model is extremely important because
# real-world applications are built using these same ideas,
# even when the applications become much more complex.


# ============================================================
# 38. BASIC PYTHON COMPLETE — WHAT YOU NOW KNOW
# ============================================================

# You have now covered the core Python building blocks:
#
# 01. print()
# 02. Variables
# 03. Data Types
# 04. Strings
# 05. Operators
# 06. Lists
# 07. Tuples
# 08. Sets
# 09. Dictionaries
# 10. Conditions
# 11. match
# 12. for loops
# 13. while loops
# 14. break
# 15. continue
# 16. range()
# 17. enumerate()
#
# These are the foundations you need before moving
# into practical Python programming.


# ============================================================
# KEY TAKEAWAYS
# ============================================================

# 1. if / elif / else
#    -> Use these when your program needs to make decisions.
#
# 2. match / case
#    -> Useful when comparing one value against several
#       specific possible values.
#
# 3. for loop
#    -> Best for iterating through collections and ranges.
#
# 4. while loop
#    -> Best when repetition depends on a condition.
#
# 5. break
#    -> Immediately stops a loop.
#
# 6. continue
#    -> Skips the current iteration and continues the loop.
#
# 7. range()
#    -> Generates a sequence of numbers, commonly used
#       with for loops.
#
# 8. enumerate()
#    -> Gives both index and value while looping.
#
# 9. Nested loops
#    -> A loop inside another loop.
#
# 10. Loop else
#     -> Runs when the loop completes normally.
#
# 11. The most important mental model:
#
#     INPUT
#       ↓
#     PROCESS
#       ↓
#     DECISION
#       ↓
#     LOOP / ACTION
#       ↓
#     OUTPUT
#
# 12. THIS IS THE LAST MAJOR TOPIC IN THE BASIC PYTHON COURSE.
#
#     You do NOT need to memorize every syntax immediately.
#
#     The important thing is to understand:
#
#       "When do I use if?"
#       "When do I use match?"
#       "When do I use for?"
#       "When do I use while?"
#       "When do I use break or continue?"
#
#     You will become comfortable with the syntax by building
#     projects.
#
# ============================================================
# END OF PYTHON BASICS
# ============================================================