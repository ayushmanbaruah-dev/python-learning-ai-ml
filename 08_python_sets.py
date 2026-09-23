# ============================================================
# 09_python_sets.py
# Python Sets
#
# Description:
# Complete practice file covering Python Sets:
# - Creating sets
# - Accessing/checking set items
# - Adding items
# - Removing items
# - Joining sets
# - Set operations
# - Frozenset
# - Set methods
#
# ============================================================


# ============================================================
# 1. CREATING SETS
# ============================================================

# A set:
# - Is unordered
# - Is unindexed
# - Does not allow duplicate values
# - Can be changed by adding/removing items

fruits = {"apple", "banana", "cherry"}

print("Fruits:", fruits)


# Duplicate values are automatically removed.

fruits = {"apple", "banana", "cherry", "apple"}

print("Duplicates removed:", fruits)


# A set can contain different data types.

mixed_set = {"Aayushman", 22, 85.5, True}

print("Mixed set:", mixed_set)


# ============================================================
# 2. SET LENGTH
# ============================================================

fruits = {"apple", "banana", "cherry"}

print("Number of fruits:", len(fruits))


# ============================================================
# 3. CHECK SET TYPE
# ============================================================

print("Type:", type(fruits))


# ============================================================
# 4. CREATING A SET USING set()
# ============================================================

fruits = set(("apple", "banana", "cherry"))

print("Set created using set():", fruits)


# Creating a set from a list

numbers = [1, 2, 2, 3, 3, 4, 4]

unique_numbers = set(numbers)

print("Original list:", numbers)
print("Unique numbers:", unique_numbers)


# ============================================================
# 5. IMPORTANT: EMPTY SET
# ============================================================

# {} creates an empty dictionary, NOT an empty set.

empty_dictionary = {}

print("Type of {}:", type(empty_dictionary))


# To create an empty set:

empty_set = set()

print("Empty set:", empty_set)
print("Type:", type(empty_set))


# ============================================================
# 6. ACCESSING SET ITEMS
# ============================================================

# Sets do NOT support indexing.

fruits = {"apple", "banana", "cherry"}

# This would cause an error:
#
# print(fruits[0])


# Instead, loop through the set.

for fruit in fruits:
    print("Fruit:", fruit)


# ============================================================
# 7. CHECK IF AN ITEM EXISTS
# ============================================================

fruits = {"apple", "banana", "cherry"}

if "apple" in fruits:
    print("Apple exists.")

if "mango" not in fruits:
    print("Mango does not exist.")


# ============================================================
# 8. ADDING ITEMS
# ============================================================

fruits = {"apple", "banana", "cherry"}

# add() adds ONE item.

fruits.add("orange")

print("After add():", fruits)


# Adding an existing item does not create a duplicate.

fruits.add("apple")

print("After adding duplicate:", fruits)


# ============================================================
# 9. ADDING MULTIPLE ITEMS
# ============================================================

fruits = {"apple", "banana", "cherry"}

more_fruits = {"orange", "mango", "grape"}

# update() adds items from another iterable.

fruits.update(more_fruits)

print("After update():", fruits)


# update() can also accept a list.

fruits.update(["watermelon", "papaya"])

print("After updating with list:", fruits)


# ============================================================
# 10. REMOVING ITEMS
# ============================================================

fruits = {"apple", "banana", "cherry", "orange"}


# remove()
# Removes a specific item.
# Raises an error if the item does not exist.

fruits.remove("banana")

print("After remove():", fruits)


# discard()
# Removes a specific item.
# Does NOT raise an error if the item doesn't exist.

fruits.discard("apple")

print("After discard():", fruits)

fruits.discard("mango")

print("Discarding missing item:", fruits)


# ============================================================
# 11. pop()
# ============================================================

fruits = {"apple", "banana", "cherry"}

# pop() removes and returns an arbitrary item.
# Because sets are unordered, don't rely on which item is removed.

removed_item = fruits.pop()

print("Removed item:", removed_item)
print("Remaining fruits:", fruits)


# ============================================================
# 12. clear()
# ============================================================

fruits = {"apple", "banana", "cherry"}

fruits.clear()

print("After clear():", fruits)


# ============================================================
# 13. del
# ============================================================

fruits = {"apple", "banana", "cherry"}

del fruits

# The set no longer exists.


# ============================================================
# 14. UNION
# ============================================================

# union() combines all unique values from two or more sets.

set1 = {"apple", "banana", "cherry"}
set2 = {"orange", "banana", "mango"}

result = set1.union(set2)

print("Union:", result)


# Using | operator

result = set1 | set2

print("Union using |:", result)


# IMPORTANT:
# union() returns a NEW set.
# It does not modify the original sets.


# ============================================================
# 15. UPDATE
# ============================================================

set1 = {"apple", "banana"}
set2 = {"cherry", "orange"}

set1.update(set2)

print("After update():", set1)


# IMPORTANT:
# update() changes the original set.


# ============================================================
# 16. INTERSECTION
# ============================================================

# intersection() returns ONLY values that exist
# in BOTH sets.

set1 = {"apple", "banana", "cherry"}
set2 = {"banana", "cherry", "orange"}

common = set1.intersection(set2)

print("Intersection:", common)


# Using & operator

common = set1 & set2

print("Intersection using &:", common)


# ============================================================
# 17. DIFFERENCE
# ============================================================

# difference() returns items that exist in the FIRST set
# but NOT in the second set.

set1 = {"apple", "banana", "cherry"}
set2 = {"banana", "orange"}

result = set1.difference(set2)

print("Difference:", result)


# Using - operator

result = set1 - set2

print("Difference using -:", result)


# ============================================================
# 18. SYMMETRIC DIFFERENCE
# ============================================================

# symmetric_difference() returns values that exist
# in either set, but NOT in both.

set1 = {"apple", "banana", "cherry"}
set2 = {"banana", "orange", "mango"}

result = set1.symmetric_difference(set2)

print("Symmetric difference:", result)


# Using ^ operator

result = set1 ^ set2

print("Symmetric difference using ^:", result)


# ============================================================
# 19. PRACTICAL EXAMPLE - UNIQUE SKILLS
# ============================================================

skills = [
    "Python",
    "SQL",
    "Python",
    "Machine Learning",
    "SQL",
    "Pandas"
]

unique_skills = set(skills)

print("Original skills:", skills)
print("Unique skills:", unique_skills)


# This is one of the most useful real-world uses of sets:
# removing duplicate values.


# ============================================================
# 20. PRACTICAL EXAMPLE - COMMON SKILLS
# ============================================================

candidate1_skills = {
    "Python",
    "SQL",
    "Pandas",
    "Machine Learning"
}

candidate2_skills = {
    "Python",
    "SQL",
    "TensorFlow",
    "Deep Learning"
}

common_skills = candidate1_skills.intersection(candidate2_skills)

print("Common skills:", common_skills)


# ============================================================
# 21. PRACTICAL EXAMPLE - UNIQUE USERS
# ============================================================

website_visitors = [
    "user101",
    "user102",
    "user101",
    "user103",
    "user102",
    "user104"
]

unique_visitors = set(website_visitors)

print("Total visits:", len(website_visitors))
print("Unique visitors:", len(unique_visitors))
print("Unique visitor IDs:", unique_visitors)


# ============================================================
# 22. SET SUBSET
# ============================================================

# issubset() checks whether every item in one set
# exists inside another set.

required_skills = {"Python", "SQL"}

candidate_skills = {
    "Python",
    "SQL",
    "Pandas",
    "Machine Learning"
}

print(
    "Has required skills:",
    required_skills.issubset(candidate_skills)
)


# ============================================================
# 23. SET SUPERSET
# ============================================================

print(
    "Candidate skills contain all required skills:",
    candidate_skills.issuperset(required_skills)
)


# ============================================================
# 24. DISJOINT SETS
# ============================================================

# isdisjoint() returns True if two sets have NO
# common elements.

set1 = {"apple", "banana"}
set2 = {"orange", "mango"}

print(
    "Are sets disjoint?",
    set1.isdisjoint(set2)
)


# ============================================================
# 25. FROZENSET
# ============================================================

# ============================================================
# ⭐ IMPORTANT TOPIC: FROZENSET
# ============================================================

# A frozenset is an IMMUTABLE version of a set.
#
# Set:
#     Mutable
#     Can add/remove items
#
# Frozenset:
#     Immutable
#     Cannot add/remove items
#
# Both:
#     - Store unique values
#     - Are unordered
#     - Support set operations
#
# W3Schools describes frozenset as an immutable version
# of a set.
#
# ============================================================


# Creating a frozenset

fruits = frozenset({"apple", "banana", "cherry"})

print("Frozenset:", fruits)
print("Type:", type(fruits))


# ============================================================
# 26. WHY DO WE NEED FROZENSET?
# ============================================================

# The main reason:
#
# Sometimes you want a collection of UNIQUE values,
# but you do NOT want anyone to modify those values.
#
# A normal set can be changed:
#
# my_set.add(...)
# my_set.remove(...)
#
# A frozenset cannot be changed.
#
# This makes frozenset useful when the collection should
# remain fixed.


# ============================================================
# 27. FROZENSET CANNOT BE MODIFIED
# ============================================================

skills = frozenset({
    "Python",
    "SQL",
    "Pandas"
})

# The following operations are NOT allowed:
#
# skills.add("Machine Learning")
# skills.remove("SQL")
#
# They would raise AttributeError.


# ============================================================
# 28. WHEN SHOULD YOU USE FROZENSET?
# ============================================================

# USE FROZENSET WHEN:
#
# 1. You need UNIQUE values.
#
# 2. You want those values to remain unchanged.
#
# 3. You need a set-like object that can be safely used
#    where a hashable value is required.
#
# 4. You want to use a set as an element inside another
#    set or as a dictionary key.
#
# ============================================================


# ============================================================
# 29. IMPORTANT: FROZENSET AS A SET ELEMENT
# ============================================================

# A normal set cannot contain another mutable set because
# normal sets are not hashable.
#
# But a frozenset CAN be stored inside a set.

group1 = frozenset({"Python", "SQL"})
group2 = frozenset({"Pandas", "NumPy"})

skill_groups = {group1, group2}

print("Set containing frozensets:", skill_groups)


# ============================================================
# 30. FROZENSET AS A DICTIONARY KEY
# ============================================================

# Because frozensets are immutable/hashable, they can be
# used as dictionary keys.

permissions = {
    frozenset({"read", "write"}): "Editor",
    frozenset({"read"}): "Viewer"
}

print("Permissions:", permissions)


# ============================================================
# 31. FROZENSET FROM A LIST
# ============================================================

skills_list = [
    "Python",
    "SQL",
    "Python",
    "Pandas"
]

skills_frozen = frozenset(skills_list)

print("Original list:", skills_list)
print("Frozenset:", skills_frozen)


# ============================================================
# 32. FROZENSET OPERATIONS
# ============================================================

skills1 = frozenset({"Python", "SQL", "Pandas"})
skills2 = frozenset({"Python", "TensorFlow", "SQL"})

print("Union:", skills1.union(skills2))

print("Intersection:", skills1.intersection(skills2))

print("Difference:", skills1.difference(skills2))

print(
    "Symmetric difference:",
    skills1.symmetric_difference(skills2)
)


# ============================================================
# 33. SET VS FROZENSET
# ============================================================

"""
SET
------------------------------------------------------------
my_set = {"Python", "SQL"}

Mutable:
    my_set.add("Pandas")
    my_set.remove("SQL")

Use when:
    You need a collection of unique values
    that may change.


FROZENSET
------------------------------------------------------------
my_frozenset = frozenset({"Python", "SQL"})

Immutable:
    Cannot add
    Cannot remove

Use when:
    You need unique values
    AND
    you want the collection to remain fixed.

    It can also be used in contexts requiring a
    hashable object, such as a dictionary key or
    an element inside another set.
"""


# ============================================================
# 34. SET METHODS
# ============================================================

"""
Python Set Methods:

add()
    Adds an element.

clear()
    Removes all elements.

copy()
    Returns a copy of the set.

difference()
    Returns items only in the first set.

difference_update()
    Removes items found in another set.

discard()
    Removes an item without raising an error
    if the item does not exist.

intersection()
    Returns items common to both sets.

intersection_update()
    Keeps only common items in the original set.

isdisjoint()
    Checks whether two sets have no common items.

issubset()
    Checks whether one set is contained in another.

issuperset()
    Checks whether one set contains another set.

pop()
    Removes and returns an arbitrary item.

remove()
    Removes a specific item and raises an error
    if it does not exist.

symmetric_difference()
    Returns items that are in either set,
    but not both.

symmetric_difference_update()
    Updates the original set with symmetric difference.

union()
    Returns all unique items from sets.

update()
    Adds items from another iterable.
"""


# ============================================================
# 35. QUICK SET METHODS PRACTICE
# ============================================================

numbers = {10, 20, 30, 40}

numbers.add(50)
print("add():", numbers)

numbers.update([60, 70])
print("update():", numbers)

numbers.remove(10)
print("remove():", numbers)

numbers.discard(20)
print("discard():", numbers)

print("copy():", numbers.copy())

print("isdisjoint():", numbers.isdisjoint({100, 200}))

print(
    "issubset():",
    {30, 40}.issubset(numbers)
)

print(
    "issuperset():",
    numbers.issuperset({30, 40})
)


# ============================================================
# KEY TAKEAWAYS
# ============================================================

# 1. A set stores UNIQUE values.
#
# 2. Sets do not allow duplicate values.
#
# 3. Sets are unordered and unindexed.
#
# 4. You cannot access a set using:
#       set[0]
#
# 5. Use "in" to check whether an item exists.
#
# 6. add() adds one item.
#
# 7. update() adds multiple items.
#
# 8. remove() removes an item and raises an error
#    if the item doesn't exist.
#
# 9. discard() removes an item without raising an error
#    if the item doesn't exist.
#
# 10. pop() removes an arbitrary item.
#
# 11. clear() empties the set.
#
# 12. union() combines unique values.
#
# 13. intersection() finds common values.
#
# 14. difference() finds values only in the first set.
#
# 15. symmetric_difference() finds values that are
#     different between the two sets.
#
# 16. issubset() checks whether one set is contained
#     inside another.
#
# 17. issuperset() checks whether one set contains
#     another set.
#
# 18. isdisjoint() checks whether two sets have
#     no common values.
#
# ------------------------------------------------------------
# ⭐ FROZENSET
# ------------------------------------------------------------
#
# 19. frozenset is an IMMUTABLE set.
#
# 20. A frozenset:
#     - Has unique values
#     - Is unordered
#     - Cannot be modified
#
# 21. You cannot use:
#       frozenset.add()
#       frozenset.remove()
#
# 22. Use frozenset when you need:
#     UNIQUE + FIXED data.
#
# 23. A frozenset can be used as:
#     - A dictionary key
#     - An element inside another set
#
# 24. Normal set:
#
#     my_set = {"Python", "SQL"}
#
#     Use when the collection may change.
#
# 25. Frozenset:
#
#     my_set = frozenset({"Python", "SQL"})
#
#     Use when the collection should remain unchanged.
#
# 26. You don't need to memorize every set method now.
#     Understand what problem each operation solves.
#
# ============================================================