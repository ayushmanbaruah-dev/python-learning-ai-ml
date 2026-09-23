# ============================================================
# 03_python_datatypes.py
# Python Data Types
# Source: W3Schools - Python Data Types
# ============================================================


# ------------------------------------------------------------
# 1. Checking the Data Type
# ------------------------------------------------------------

x = 5

print(x)
print(type(x))


# ------------------------------------------------------------
# 2. Text Type - str
# ------------------------------------------------------------

name = "Aayushman"

print(name)
print(type(name))


# ------------------------------------------------------------
# 3. Numeric Types
# ------------------------------------------------------------

# Integer
age = 22

# Float
height = 5.8

# Complex
complex_number = 1j

print(age)
print(type(age))

print(height)
print(type(height))

print(complex_number)
print(type(complex_number))


# ------------------------------------------------------------
# 4. Sequence Types
# ------------------------------------------------------------

# List
fruits_list = ["apple", "banana", "cherry"]

print(fruits_list)
print(type(fruits_list))


# Tuple
fruits_tuple = ("apple", "banana", "cherry")

print(fruits_tuple)
print(type(fruits_tuple))


# Range
numbers_range = range(6)

print(numbers_range)
print(type(numbers_range))


# ------------------------------------------------------------
# 5. Mapping Type - dict
# ------------------------------------------------------------

student = {
    "name": "Aayushman",
    "age": 22,
    "course": "Data Science"
}

print(student)
print(type(student))


# ------------------------------------------------------------
# 6. Set Types
# ------------------------------------------------------------

# Set
fruits_set = {"apple", "banana", "cherry"}

print(fruits_set)
print(type(fruits_set))


# Frozen Set
fruits_frozen_set = frozenset(
    {"apple", "banana", "cherry"}
)

print(fruits_frozen_set)
print(type(fruits_frozen_set))


# ------------------------------------------------------------
# 7. Boolean Type - bool
# ------------------------------------------------------------

is_learning_python = True
is_sleeping = False

print(is_learning_python)
print(type(is_learning_python))

print(is_sleeping)
print(type(is_sleeping))


# ------------------------------------------------------------
# 8. Binary Types
# ------------------------------------------------------------

# Bytes
data_bytes = b"Hello"

print(data_bytes)
print(type(data_bytes))


# Bytearray
data_bytearray = bytearray(5)

print(data_bytearray)
print(type(data_bytearray))


# Memoryview
data_memoryview = memoryview(bytes(5))

print(data_memoryview)
print(type(data_memoryview))


# ------------------------------------------------------------
# 9. None Type
# ------------------------------------------------------------

result = None

print(result)
print(type(result))


# ------------------------------------------------------------
# 10. Setting Specific Data Types
# ------------------------------------------------------------

text = str("Hello World")
integer_number = int(20)
decimal_number = float(20.5)
complex_value = complex(1j)

print(text)
print(integer_number)
print(decimal_number)
print(complex_value)


# ------------------------------------------------------------
# 11. Creating List and Tuple Using Constructors
# ------------------------------------------------------------

my_list = list(("apple", "banana", "cherry"))
my_tuple = tuple(("apple", "banana", "cherry"))

print(my_list)
print(type(my_list))

print(my_tuple)
print(type(my_tuple))


# ------------------------------------------------------------
# 12. Creating Range and Dictionary
# ------------------------------------------------------------

my_range = range(6)

my_dictionary = dict(
    name="Aayushman",
    age=22
)

print(my_range)
print(type(my_range))

print(my_dictionary)
print(type(my_dictionary))


# ------------------------------------------------------------
# 13. Creating Set and Frozen Set
# ------------------------------------------------------------

my_set = set(("apple", "banana", "cherry"))

my_frozen_set = frozenset(
    ("apple", "banana", "cherry")
)

print(my_set)
print(type(my_set))

print(my_frozen_set)
print(type(my_frozen_set))


# ------------------------------------------------------------
# 14. Practical Example
# ------------------------------------------------------------

student_name = "Aayushman"       # str
student_age = 22                 # int
student_height = 5.8             # float
student_courses = ["Python", "SQL", "Machine Learning"]  # list
student_details = {
    "name": "Aayushman",
    "age": 22
}                                # dict
is_student = True                # bool

print("Name:", student_name)
print("Age:", student_age)
print("Height:", student_height)
print("Courses:", student_courses)
print("Details:", student_details)
print("Is Student:", is_student)


# ============================================================
# KEY TAKEAWAYS
# ============================================================
#
# 1. Every value in Python has a data type.
#
# 2. Use type() to check the data type of a value.
#
# 3. Python's built-in data types include:
#
#    Text:
#    - str
#
#    Numeric:
#    - int
#    - float
#    - complex
#
#    Sequence:
#    - list
#    - tuple
#    - range
#
#    Mapping:
#    - dict
#
#    Set:
#    - set
#    - frozenset
#
#    Boolean:
#    - bool
#
#    Binary:
#    - bytes
#    - bytearray
#    - memoryview
#
#    None:
#    - NoneType
#
# 4. The data type is normally determined when you assign
#    a value to a variable.
#
# 5. Python provides constructor functions such as:
#    str(), int(), float(), list(), tuple(), dict(),
#    set(), bool(), bytes(), etc.
#
# 6. Important distinction:
#
#    22      -> int
#    22.0    -> float
#    "22"    -> str
#    True    -> bool
#    None    -> NoneType
#
# 7. Lists, tuples, dictionaries, and sets are important
#    collection types that we will use heavily later.
#
# ============================================================