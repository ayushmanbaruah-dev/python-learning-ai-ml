# ============================================================
# 05_python_operators.py
# Python Operators
# Source: W3Schools - Python Operators
# ============================================================


# ------------------------------------------------------------
# 1. Arithmetic Operators
# ------------------------------------------------------------

a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)
print("Floor Division:", a // b)


# ------------------------------------------------------------
# 2. Assignment Operators
# ------------------------------------------------------------

x = 10
print("x =", x)

x += 5
print("x += 5:", x)

x -= 3
print("x -= 3:", x)

x *= 2
print("x *= 2:", x)

x /= 4
print("x /= 4:", x)

x //= 2
print("x //= 2:", x)

x %= 3
print("x %= 3:", x)

x **= 2
print("x **= 2:", x)


# Assignment with bitwise operators

number = 10

number &= 6
print("number &= 6:", number)

number = 10
number |= 6
print("number |= 6:", number)

number = 10
number ^= 6
print("number ^= 6:", number)

number = 10
number >>= 1
print("number >>= 1:", number)

number = 10
number <<= 1
print("number <<= 1:", number)


# ------------------------------------------------------------
# 3. Comparison Operators
# ------------------------------------------------------------

a = 10
b = 5

print("Equal:", a == b)
print("Not Equal:", a != b)
print("Greater Than:", a > b)
print("Less Than:", a < b)
print("Greater Than or Equal:", a >= b)
print("Less Than or Equal:", a <= b)


# ------------------------------------------------------------
# 4. Logical Operators
# ------------------------------------------------------------

age = 22
has_id = True

print("AND:", age >= 18 and has_id)
print("OR:", age >= 18 or has_id)
print("NOT:", not has_id)


# More logical operator examples

temperature = 25

print(temperature > 20 and temperature < 30)
print(temperature < 10 or temperature > 35)
print(not temperature < 10)


# ------------------------------------------------------------
# 5. Identity Operators
# ------------------------------------------------------------

x = ["Python", "SQL"]
y = ["Python", "SQL"]
z = x

print("x is y:", x is y)
print("x is z:", x is z)

print("x is not y:", x is not y)
print("x is not z:", x is not z)


# ------------------------------------------------------------
# 6. Membership Operators
# ------------------------------------------------------------

# Membership operators are also part of Python operators.

fruits = ["apple", "banana", "cherry"]

print("apple in fruits:", "apple" in fruits)
print("orange in fruits:", "orange" in fruits)

print("orange not in fruits:", "orange" not in fruits)


# Membership with strings

text = "Python Programming"

print("Python" in text)
print("Java" in text)
print("Java" not in text)


# ------------------------------------------------------------
# 7. Bitwise Operators
# ------------------------------------------------------------

a = 10
b = 3

print("AND:", a & b)
print("OR:", a | b)
print("XOR:", a ^ b)
print("NOT:", ~a)
print("Left Shift:", a << 1)
print("Right Shift:", a >> 1)


# ------------------------------------------------------------
# 8. Operator Precedence
# ------------------------------------------------------------

# Multiplication happens before addition.

result = 10 + 5 * 2

print("10 + 5 * 2 =", result)


# Parentheses have higher priority.

result = (10 + 5) * 2

print("(10 + 5) * 2 =", result)


# More examples

result = 20 - 5 * 2
print("20 - 5 * 2 =", result)

result = (20 - 5) * 2
print("(20 - 5) * 2 =", result)


# ------------------------------------------------------------
# 9. Precedence With Multiple Operators
# ------------------------------------------------------------

result = 10 + 2 * 3 ** 2

print("10 + 2 * 3 ** 2 =", result)


# Parentheses can change the order.

result = (10 + 2) * 3 ** 2

print("(10 + 2) * 3 ** 2 =", result)


# ------------------------------------------------------------
# 10. Comparison + Logical Operators
# ------------------------------------------------------------

age = 22
salary = 50000

result = age >= 18 and salary >= 30000

print("Eligible:", result)


# ------------------------------------------------------------
# 11. Practical Example
# ------------------------------------------------------------

marks = 85
attendance = 90

passed_marks = marks >= 40
passed_attendance = attendance >= 75

passed = passed_marks and passed_attendance

print("Marks:", marks)
print("Attendance:", attendance)
print("Passed Marks Requirement:", passed_marks)
print("Passed Attendance Requirement:", passed_attendance)
print("Final Result:", passed)


# ============================================================
# KEY TAKEAWAYS
# ============================================================
#
# 1. Operators are symbols/keywords used to perform operations
#    on values and variables.
#
# 2. Arithmetic operators:
#
#    +   Addition
#    -   Subtraction
#    *   Multiplication
#    /   Division
#    %   Modulus
#    **  Exponentiation
#    //  Floor Division
#
# 3. Assignment operators are used to assign and update values.
#
#    =
#    +=
#    -=
#    *=
#    /=
#    %=
#    //=
#    **=
#
# 4. Comparison operators return True or False.
#
#    ==
#    !=
#    >
#    <
#    >=
#    <=
#
# 5. Logical operators:
#
#    and
#    or
#    not
#
# 6. Identity operators:
#
#    is
#    is not
#
#    They check whether two variables refer to the same
#    object, not simply whether their values look the same.
#
# 7. Membership operators:
#
#    in
#    not in
#
#    They check whether a value exists inside a sequence,
#    collection, or string.
#
# 8. Bitwise operators work at the binary/bit level:
#
#    &
#    |
#    ^
#    ~
#    <<
#    >>
#
# 9. Operator precedence determines the order in which
#    Python evaluates an expression.
#
# 10. Parentheses have very high precedence and can be used
#     to explicitly control the order of operations.
#
#     (10 + 5) * 2
#
#     is different from:
#
#     10 + 5 * 2
#
# 11. A useful basic precedence order to remember is:
#
#     Parentheses
#          ↓
#     Exponentiation
#          ↓
#     Multiplication / Division / Floor Division / Modulus
#          ↓
#     Addition / Subtraction
#          ↓
#     Comparisons
#          ↓
#     not
#          ↓
#     and
#          ↓
#     or
#
# 12. When an expression becomes complicated, use
#     parentheses to make the intended order clear.
#
# 13. Operators are fundamental to programming because they
#     are used in calculations, conditions, comparisons,
#     data processing, and decision-making.
#
# ============================================================