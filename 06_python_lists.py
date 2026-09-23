# ============================================================
# 06_python_lists.py
# Python Lists
#
# Description:
# Complete practice file covering Python Lists:
# - Creating lists
# - Accessing list items
# - Changing list items
# - Adding items
# - Removing items
# - List comprehension
# - Copying lists
# - List methods
#
# ============================================================


# ============================================================
# 1. CREATING LISTS
# ============================================================

# A list stores multiple values in a single variable.
# Lists are ordered, changeable (mutable), and allow duplicates.

fruits = ["apple", "banana", "cherry"]

print("Fruits:", fruits)

# A list can contain different data types.
mixed_list = ["Aayushman", 22, 85.5, True]

print("Mixed List:", mixed_list)


# ============================================================
# 2. ACCESSING LIST ITEMS
# ============================================================

fruits = ["apple", "banana", "cherry", "orange"]

# Positive indexing starts from 0.
print("First fruit:", fruits[0])
print("Second fruit:", fruits[1])

# Negative indexing starts from the end.
print("Last fruit:", fruits[-1])
print("Second-last fruit:", fruits[-2])


# Slicing
print("First three fruits:", fruits[0:3])

print("From second item:", fruits[1:])

print("Up to third item:", fruits[:3])

# Copy using slicing
print("All fruits:", fruits[:])


# ============================================================
# 3. CHECKING IF AN ITEM EXISTS
# ============================================================

if "apple" in fruits:
    print("Apple is in the list.")

if "mango" not in fruits:
    print("Mango is not in the list.")


# ============================================================
# 4. CHANGING LIST ITEMS
# ============================================================

fruits = ["apple", "banana", "cherry"]

# Change one item
fruits[1] = "mango"

print("After changing second item:", fruits)

# Change multiple items
fruits[0:2] = ["orange", "grape"]

print("After changing multiple items:", fruits)


# ============================================================
# 5. ADDING LIST ITEMS
# ============================================================

fruits = ["apple", "banana", "cherry"]

# append() adds an item to the end.
fruits.append("orange")

print("After append:", fruits)

# insert() adds an item at a specific position.
fruits.insert(1, "mango")

print("After insert:", fruits)

# extend() adds multiple items.
more_fruits = ["grape", "watermelon"]

fruits.extend(more_fruits)

print("After extend:", fruits)


# ============================================================
# 6. REMOVING LIST ITEMS
# ============================================================

fruits = ["apple", "banana", "cherry", "orange"]

# remove() removes a specific value.
fruits.remove("banana")

print("After remove:", fruits)

# pop() removes an item using its index.
fruits.pop(1)

print("After pop:", fruits)

# If no index is provided, pop() removes the last item.
fruits.pop()

print("After removing last item:", fruits)

# del removes an item using its index.
fruits = ["apple", "banana", "cherry"]

del fruits[0]

print("After del:", fruits)

# clear() removes all items.
fruits.clear()

print("After clear:", fruits)


# ============================================================
# 7. LIST COMPREHENSION
# ============================================================

# List comprehension provides a shorter way to create lists.

numbers = [1, 2, 3, 4, 5]

squares = [number * number for number in numbers]

print("Squares:", squares)


# With a condition
even_numbers = [number for number in numbers if number % 2 == 0]

print("Even numbers:", even_numbers)


# Convert words to uppercase
names = ["aayushman", "rahul", "amit"]

uppercase_names = [name.upper() for name in names]

print("Uppercase names:", uppercase_names)


# ============================================================
# 8. LIST COMPREHENSION WITH RANGE
# ============================================================

numbers = [number for number in range(1, 11)]

print("Numbers 1-10:", numbers)

squares = [number ** 2 for number in range(1, 11)]

print("Squares 1-10:", squares)

even_numbers = [number for number in range(1, 21) if number % 2 == 0]

print("Even numbers 1-20:", even_numbers)


# ============================================================
# 9. COPYING LISTS
# ============================================================

original = ["apple", "banana", "cherry"]

# Using copy()
copied_list = original.copy()

print("Original:", original)
print("Copied:", copied_list)


# Using list()
copied_list_2 = list(original)

print("Second copy:", copied_list_2)


# Using slicing
copied_list_3 = original[:]

print("Third copy:", copied_list_3)


# Important:
# Do NOT do this if you want an independent copy:
#
# copied_list = original
#
# This creates another reference to the same list.


# ============================================================
# 10. LIST LENGTH
# ============================================================

students = ["Aayushman", "Rahul", "Amit", "Priya"]

print("Number of students:", len(students))


# ============================================================
# 11. LOOPING THROUGH A LIST
# ============================================================

for student in students:
    print("Student:", student)


# Using index
for index in range(len(students)):
    print(index, students[index])


# Using enumerate()
for index, student in enumerate(students):
    print(index, student)


# ============================================================
# 12. SORTING LISTS
# ============================================================

numbers = [50, 10, 40, 20, 30]

numbers.sort()

print("Sorted numbers:", numbers)

numbers.sort(reverse=True)

print("Descending numbers:", numbers)


# sorted() creates a new sorted list.
numbers = [50, 10, 40, 20, 30]

sorted_numbers = sorted(numbers)

print("Original:", numbers)
print("Sorted copy:", sorted_numbers)


# ============================================================
# 13. REVERSE A LIST
# ============================================================

fruits = ["apple", "banana", "cherry"]

fruits.reverse()

print("Reversed fruits:", fruits)


# ============================================================
# 14. COUNT AND INDEX
# ============================================================

numbers = [10, 20, 30, 20, 40, 20]

print("Number of 20s:", numbers.count(20))

print("Index of 30:", numbers.index(30))


# ============================================================
# 15. NESTED LISTS
# ============================================================

students = [
    ["Aayushman", 85],
    ["Rahul", 90],
    ["Amit", 78]
]

print("First student:", students[0])

print("First student's name:", students[0][0])

print("First student's marks:", students[0][1])


# ============================================================
# 16. PRACTICAL EXAMPLE - STUDENT MARKS
# ============================================================

marks = [85, 78, 92, 88, 76]

total = sum(marks)
average = total / len(marks)

print("Marks:", marks)
print("Total:", total)
print("Average:", average)
print("Highest:", max(marks))
print("Lowest:", min(marks))


# ============================================================
# 17. PRACTICAL EXAMPLE - FILTERING DATA
# ============================================================

marks = [35, 67, 82, 45, 29, 91, 73]

passed_marks = [mark for mark in marks if mark >= 40]

failed_marks = [mark for mark in marks if mark < 40]

print("Passed marks:", passed_marks)
print("Failed marks:", failed_marks)


# ============================================================
# 18. PRACTICAL EXAMPLE - EXPENSE TRACKER
# ============================================================

expenses = [250, 500, 120, 800, 300]

total_expenses = sum(expenses)
average_expense = total_expenses / len(expenses)
highest_expense = max(expenses)

print("Expenses:", expenses)
print("Total expenses:", total_expenses)
print("Average expense:", average_expense)
print("Highest expense:", highest_expense)


# ============================================================
# 19. LIST METHODS
# ============================================================

# The following section is intentionally kept as the
# dedicated List Methods reference section.

"""
Python List Methods:

append()      Add an item to the end of the list
clear()       Remove all items from the list
copy()        Return a copy of the list
count()       Return the number of times a value appears
extend()      Add items from another iterable
index()       Return the index of the first matching value
insert()      Add an item at a specific position
pop()         Remove and return an item
remove()      Remove the first matching value
reverse()     Reverse the order of the list
sort()        Sort the list
"""


# ============================================================
# 20. QUICK LIST METHODS EXAMPLE
# ============================================================

numbers = [30, 10, 20, 40]

numbers.append(50)
print("append():", numbers)

numbers.insert(1, 15)
print("insert():", numbers)

numbers.extend([60, 70])
print("extend():", numbers)

numbers.remove(15)
print("remove():", numbers)

removed_value = numbers.pop()
print("pop():", numbers)
print("Removed value:", removed_value)

print("count():", numbers.count(20))
print("index():", numbers.index(20))

numbers.sort()
print("sort():", numbers)

numbers.reverse()
print("reverse():", numbers)

copied_numbers = numbers.copy()
print("copy():", copied_numbers)

numbers.clear()
print("clear():", numbers)


# ============================================================
# KEY TAKEAWAYS
# ============================================================

# 1. A list stores multiple values in one variable.
#
# 2. Lists are:
#    - Ordered
#    - Changeable (mutable)
#    - Allow duplicate values
#
# 3. Indexing starts at 0.
#
# 4. Negative indexing starts from the end.
#
# 5. Slicing allows you to access a range of items.
#
# 6. Use append() to add one item.
#
# 7. Use extend() to add multiple items.
#
# 8. Use insert() to add an item at a specific position.
#
# 9. Use remove() to remove a specific value.
#
# 10. Use pop() to remove an item by index.
#
# 11. Use del to delete an item or an entire list.
#
# 12. Use clear() to empty a list.
#
# 13. List comprehension provides a concise way to create lists.
#
# 14. Use copy() when you need an independent copy of a list.
#
# 15. len() returns the number of items in a list.
#
# 16. sum(), min(), and max() are useful for numerical lists.
#
# 17. sort() changes the original list.
#
# 18. sorted() returns a new sorted list.
#
# 19. enumerate() is useful when you need both index and value.
#
# 20. Lists are heavily used in real Python applications,
#     data analysis, automation, and machine learning.
#
# ============================================================