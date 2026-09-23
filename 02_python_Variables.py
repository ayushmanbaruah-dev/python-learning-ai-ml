# ============================================================
# 02_python_variables.py
# Python Variables
# Source: W3Schools - Python Variables
# ============================================================


# ------------------------------------------------------------
# 1. Creating Variables
# ------------------------------------------------------------

name = "Aayushman"
age = 22
height = 5.8

print(name)
print(age)
print(height)


# ------------------------------------------------------------
# 2. Assigning Multiple Variables
# ------------------------------------------------------------

first_name, last_name, age = "Aayushman", "Baruah", 22

print(first_name)
print(last_name)
print(age)


# ------------------------------------------------------------
# 3. Assigning the Same Value to Multiple Variables
# ------------------------------------------------------------

x = y = z = 100

print(x)
print(y)
print(z)


# ------------------------------------------------------------
# 4. Getting the Type of a Variable
# ------------------------------------------------------------

name = "Aayushman"
age = 22
height = 5.8
is_learning = True

print(type(name))
print(type(age))
print(type(height))
print(type(is_learning))


# ------------------------------------------------------------
# 5. Variables Are Dynamically Typed
# ------------------------------------------------------------

value = 10

print(value)
print(type(value))

value = "Python"

print(value)
print(type(value))


# ------------------------------------------------------------
# 6. Casting
# ------------------------------------------------------------

number_as_string = "22"

number = int(number_as_string)
decimal_number = float(number_as_string)
text = str(22)

print(number)
print(decimal_number)
print(text)

print(type(number))
print(type(decimal_number))
print(type(text))


# ------------------------------------------------------------
# 7. String Variables
# ------------------------------------------------------------

name = "Aayushman"
city = 'Assam'

print(name)
print(city)


# ------------------------------------------------------------
# 8. Variable Names Are Case-Sensitive
# ------------------------------------------------------------

age = 22
Age = 25

print(age)
print(Age)


# ------------------------------------------------------------
# 9. Valid Variable Names
# ------------------------------------------------------------

user_name = "Aayushman"
user_age = 22
python_version = 3.14

print(user_name)
print(user_age)
print(python_version)


# ------------------------------------------------------------
# 10. Variable Names With Underscores
# ------------------------------------------------------------

first_name = "Aayushman"
last_name = "Baruah"

print(first_name)
print(last_name)


# ------------------------------------------------------------
# 11. Updating a Variable
# ------------------------------------------------------------

score = 10

print(score)

score = 20

print(score)

score = score + 5

print(score)


# ------------------------------------------------------------
# 12. Practical Example
# ------------------------------------------------------------

student_name = "Aayushman"
student_age = 22
student_height = 5.8
is_student = True

print("Name:", student_name)
print("Age:", student_age)
print("Height:", student_height)
print("Is Student:", is_student)
# ============================================================
# KEY TAKEAWAYS
# ============================================================
#
# 1. Variables are used to store values.
#    Example: name = "Aayushman"
#
# 2. Python variables do not need an explicit type declaration.
#
# 3. Python is dynamically typed.
#    A variable can refer to different types of values.
#
# 4. Use type() to check the type of a variable.
#
# 5. Common Python data types include:
#    - str    -> "Hello"
#    - int    -> 22
#    - float  -> 5.8
#    - bool   -> True / False
#
# 6. Casting converts a value from one type to another.
#    int(), float(), str()
#
# 7. Variable names are case-sensitive.
#    age and Age are different variables.
#
# 8. Use descriptive variable names.
#    Example: student_name instead of x
#
# 9. Underscores can be used in variable names.
#    Example: first_name
#
# 10. 22 and "22" are different:
#     22   -> integer
#     "22" -> string
#
# ============================================================