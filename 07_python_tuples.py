# ============================================================
# 07_python_tuples.py
# Python Tuples
#
# Description:
# Complete practice file covering Python Tuples:
# - Creating tuples
# - Accessing tuple items
# - Updating tuples
# - Unpacking tuples
# - Joining tuples
# - Tuple methods
#
# ============================================================


# ============================================================
# 1. CREATING TUPLES
# ============================================================

# A tuple stores multiple values in a single variable.
# Tuples are:
# - Ordered
# - Unchangeable (immutable)
# - Allow duplicate values

fruits = ("apple", "banana", "cherry")

print("Fruits:", fruits)

# Tuple with different data types
student = ("Aayushman", 22, 85.5, True)

print("Student:", student)


# ============================================================
# 2. CREATING A TUPLE WITH ONE ITEM
# ============================================================

# A comma is required when creating a one-item tuple.

one_item = ("apple",)

print("One-item tuple:", one_item)
print("Type:", type(one_item))

# Without the comma, Python treats it as a string.
not_a_tuple = ("apple")

print("Not a tuple:", not_a_tuple)
print("Type:", type(not_a_tuple))


# ============================================================
# 3. ACCESSING TUPLE ITEMS
# ============================================================

fruits = ("apple", "banana", "cherry", "orange")

# Positive indexing starts from 0.
print("First fruit:", fruits[0])
print("Second fruit:", fruits[1])

# Negative indexing starts from the end.
print("Last fruit:", fruits[-1])
print("Second-last fruit:", fruits[-2])


# ============================================================
# 4. ACCESSING A RANGE OF TUPLE ITEMS
# ============================================================

fruits = ("apple", "banana", "cherry", "orange", "mango")

# Slicing
print("First three:", fruits[0:3])

print("From second item:", fruits[1:])

print("Up to third item:", fruits[:3])

print("All items:", fruits[:])


# ============================================================
# 5. CHECKING IF AN ITEM EXISTS
# ============================================================

fruits = ("apple", "banana", "cherry")

if "apple" in fruits:
    print("Apple is in the tuple.")

if "mango" not in fruits:
    print("Mango is not in the tuple.")


# ============================================================
# 6. TUPLES ARE UNCHANGEABLE
# ============================================================

fruits = ("apple", "banana", "cherry")

# The following would cause an error:
#
# fruits[0] = "orange"
#
# Tuples cannot be changed directly after creation.


# ============================================================
# 7. UPDATING A TUPLE
# ============================================================

# Although tuples are immutable, you can convert the tuple
# to a list, make changes, and convert it back to a tuple.

fruits = ("apple", "banana", "cherry")

temporary_list = list(fruits)

temporary_list[1] = "mango"

fruits = tuple(temporary_list)

print("Updated tuple:", fruits)


# ============================================================
# 8. ADDING ITEMS TO A TUPLE
# ============================================================

fruits = ("apple", "banana", "cherry")

temporary_list = list(fruits)

temporary_list.append("orange")

fruits = tuple(temporary_list)

print("After adding item:", fruits)


# ============================================================
# 9. REMOVING ITEMS FROM A TUPLE
# ============================================================

fruits = ("apple", "banana", "cherry")

temporary_list = list(fruits)

temporary_list.remove("banana")

fruits = tuple(temporary_list)

print("After removing item:", fruits)


# ============================================================
# 10. DELETING A TUPLE
# ============================================================

fruits = ("apple", "banana", "cherry")

# You can delete the entire tuple using del.

del fruits

# The following would cause an error because the tuple no longer exists:
#
# print(fruits)


# ============================================================
# 11. UNPACKING A TUPLE
# ============================================================

# Tuple unpacking allows you to assign tuple values
# to separate variables.

fruits = ("apple", "banana", "cherry")

fruit1, fruit2, fruit3 = fruits

print("Fruit 1:", fruit1)
print("Fruit 2:", fruit2)
print("Fruit 3:", fruit3)


# ============================================================
# 12. UNPACKING USING *
# ============================================================

fruits = ("apple", "banana", "cherry", "orange", "mango")

fruit1, *remaining_fruits = fruits

print("First fruit:", fruit1)
print("Remaining fruits:", remaining_fruits)


# Another example

numbers = (10, 20, 30, 40, 50)

first, *middle, last = numbers

print("First:", first)
print("Middle:", middle)
print("Last:", last)


# ============================================================
# 13. LOOPING THROUGH A TUPLE
# ============================================================

fruits = ("apple", "banana", "cherry")

for fruit in fruits:
    print("Fruit:", fruit)


# Loop using index

for index in range(len(fruits)):
    print(index, fruits[index])


# Loop using enumerate()

for index, fruit in enumerate(fruits):
    print(index, fruit)


# ============================================================
# 14. JOINING TUPLES
# ============================================================

tuple1 = ("apple", "banana")
tuple2 = ("cherry", "orange")

joined_tuple = tuple1 + tuple2

print("Joined tuple:", joined_tuple)


# ============================================================
# 15. MULTIPLYING TUPLES
# ============================================================

fruits = ("apple", "banana")

repeated_fruits = fruits * 3

print("Repeated tuple:", repeated_fruits)


# ============================================================
# 16. TUPLE LENGTH
# ============================================================

students = ("Aayushman", "Rahul", "Amit", "Priya")

print("Number of students:", len(students))


# ============================================================
# 17. COUNT METHOD
# ============================================================

numbers = (10, 20, 20, 30, 20, 40)

count_20 = numbers.count(20)

print("Number of 20s:", count_20)


# ============================================================
# 18. INDEX METHOD
# ============================================================

numbers = (10, 20, 30, 40)

position = numbers.index(30)

print("Position of 30:", position)


# ============================================================
# 19. TUPLE METHODS
# ============================================================

"""
Python Tuple Methods:

count()     Returns the number of times a value appears
index()     Returns the index of the first matching value
"""


# ============================================================
# 20. PRACTICAL EXAMPLE - STUDENT RECORD
# ============================================================

student = ("Aayushman", 22, "Data Science", 85)

name = student[0]
age = student[1]
course = student[2]
marks = student[3]

print("Student Name:", name)
print("Age:", age)
print("Course:", course)
print("Marks:", marks)


# ============================================================
# 21. PRACTICAL EXAMPLE - COORDINATES
# ============================================================

# Tuples are commonly used to represent fixed data
# such as coordinates.

location = (22.5726, 88.3639)

latitude = location[0]
longitude = location[1]

print("Latitude:", latitude)
print("Longitude:", longitude)


# ============================================================
# 22. PRACTICAL EXAMPLE - RGB COLOR
# ============================================================

# A tuple can represent a fixed RGB color value.

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

print("Red:", red)
print("Green:", green)
print("Blue:", blue)


# ============================================================
# 23. TUPLE VS LIST
# ============================================================

# LIST
#
# my_list = [10, 20, 30]
#
# - Ordered
# - Changeable
# - Allows duplicates
#
#
# TUPLE
#
# my_tuple = (10, 20, 30)
#
# - Ordered
# - Unchangeable
# - Allows duplicates


# ============================================================
# 24. CONVERT LIST TO TUPLE
# ============================================================

numbers_list = [10, 20, 30, 40]

numbers_tuple = tuple(numbers_list)

print("List:", numbers_list)
print("Tuple:", numbers_tuple)


# ============================================================
# 25. CONVERT TUPLE TO LIST
# ============================================================

numbers_tuple = (10, 20, 30, 40)

numbers_list = list(numbers_tuple)

print("Tuple:", numbers_tuple)
print("List:", numbers_list)


# ============================================================
# KEY TAKEAWAYS
# ============================================================

# 1. A tuple stores multiple values in one variable.
#
# 2. Tuples are ordered.
#
# 3. Tuples are immutable (unchangeable).
#
# 4. Tuples allow duplicate values.
#
# 5. Tuple indexing starts at 0.
#
# 6. Negative indexing starts from the end.
#
# 7. You can use slicing with tuples.
#
# 8. A one-item tuple requires a comma:
#       ("apple",)
#
# 9. You cannot directly change, add, or remove tuple items.
#
# 10. To modify a tuple:
#       tuple -> list -> modify -> tuple
#
# 11. Tuple unpacking allows you to assign tuple values
#     to separate variables.
#
# 12. The * operator can collect multiple unpacked values.
#
# 13. Use + to join tuples.
#
# 14. Use * to repeat tuples.
#
# 15. len() returns the number of tuple items.
#
# 16. count() counts how many times a value appears.
#
# 17. index() returns the position of a value.
#
# 18. Tuples are useful for fixed data that should not change.
#
# 19. Common examples include:
#     - Coordinates
#     - RGB colors
#     - Fixed configuration values
#     - Records
#
# 20. Remember:
#
#     LIST  = changeable
#     TUPLE = unchangeable
#
# ============================================================