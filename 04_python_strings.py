# ============================================================
# 04_python_strings.py
# Python Strings
# Source: W3Schools - Python Strings
# ============================================================


# ------------------------------------------------------------
# 1. Creating Strings
# ------------------------------------------------------------

name = "Aayushman"
city = 'Assam'

print(name)
print(city)


# ------------------------------------------------------------
# 2. Multiline Strings
# ------------------------------------------------------------

message = """This is a
multiline string.
Python allows strings to span
multiple lines."""

print(message)


# ------------------------------------------------------------
# 3. Strings Are Arrays
# ------------------------------------------------------------

word = "Python"

print(word[0])
print(word[1])
print(word[5])


# ------------------------------------------------------------
# 4. Looping Through a String
# ------------------------------------------------------------

for character in "Python":
    print(character)


# ------------------------------------------------------------
# 5. String Length
# ------------------------------------------------------------

text = "Hello World!"

print(len(text))


# ------------------------------------------------------------
# 6. Checking if Text Exists
# ------------------------------------------------------------

text = "I am learning Python."

print("Python" in text)
print("Java" in text)


# ------------------------------------------------------------
# 7. Checking if Text Does Not Exist
# ------------------------------------------------------------

print("Java" not in text)
print("Python" not in text)


# ------------------------------------------------------------
# 8. Slicing Strings
# ------------------------------------------------------------

text = "Python"

print(text[0:3])
print(text[2:5])
print(text[:4])
print(text[2:])


# ------------------------------------------------------------
# 9. Negative Indexing
# ------------------------------------------------------------

text = "Python"

print(text[-1])
print(text[-2])
print(text[-6])


# ------------------------------------------------------------
# 10. Slicing With Negative Indexes
# ------------------------------------------------------------

text = "Python"

print(text[-4:-1])
print(text[:-2])
print(text[-4:])


# ------------------------------------------------------------
# 11. Uppercase
# ------------------------------------------------------------

text = "hello world"

print(text.upper())


# ------------------------------------------------------------
# 12. Lowercase
# ------------------------------------------------------------

text = "HELLO WORLD"

print(text.lower())


# ------------------------------------------------------------
# 13. Removing Whitespace
# ------------------------------------------------------------

text = "   Hello World   "

print(text.strip())


# ------------------------------------------------------------
# 14. Replacing Text
# ------------------------------------------------------------

text = "I like Java."

new_text = text.replace("Java", "Python")

print(new_text)


# ------------------------------------------------------------
# 15. Splitting Strings
# ------------------------------------------------------------

text = "apple,banana,cherry"

fruits = text.split(",")

print(fruits)


# ------------------------------------------------------------
# 16. String Concatenation
# ------------------------------------------------------------

first_name = "Aayushman"
last_name = "Baruah"

full_name = first_name + " " + last_name

print(full_name)


# ------------------------------------------------------------
# 17. Joining Strings
# ------------------------------------------------------------

words = ["Python", "is", "easy"]

sentence = " ".join(words)

print(sentence)


# ------------------------------------------------------------
# 18. Escape Characters
# ------------------------------------------------------------

text = "He said, \"Python is easy.\""

print(text)


# New line
message = "Hello\nWorld"

print(message)


# Tab
message = "Python\tProgramming"

print(message)


# Backslash
message = "C:\\Users\\Aayushman"

print(message)


# ------------------------------------------------------------
# 19. String Formatting - f-strings
# ------------------------------------------------------------

name = "Aayushman"
age = 22

message = f"My name is {name} and I am {age} years old."

print(message)


# ------------------------------------------------------------
# 20. Expressions Inside f-strings
# ------------------------------------------------------------

age = 22

print(f"Next year I will be {age + 1} years old.")


# ------------------------------------------------------------
# 21. Formatting Numbers
# ------------------------------------------------------------

price = 99.9999

print(f"The price is {price:.2f}")


# ------------------------------------------------------------
# 22. String Methods - capitalize()
# ------------------------------------------------------------

text = "hello world"

print(text.capitalize())


# ------------------------------------------------------------
# 23. String Methods - title()
# ------------------------------------------------------------

text = "python programming language"

print(text.title())


# ------------------------------------------------------------
# 24. String Methods - count()
# ------------------------------------------------------------

text = "Python is easy. Python is powerful."

print(text.count("Python"))


# ------------------------------------------------------------
# 25. String Methods - find()
# ------------------------------------------------------------

text = "I am learning Python."

print(text.find("Python"))


# ------------------------------------------------------------
# 26. String Methods - startswith()
# ------------------------------------------------------------

text = "Python Programming"

print(text.startswith("Python"))
print(text.startswith("Java"))


# ------------------------------------------------------------
# 27. String Methods - endswith()
# ------------------------------------------------------------

text = "Python.py"

print(text.endswith(".py"))
print(text.endswith(".txt"))


# ------------------------------------------------------------
# 28. String Methods - isalpha()
# ------------------------------------------------------------

text = "Python"

print(text.isalpha())


# ------------------------------------------------------------
# 29. String Methods - isdigit()
# ------------------------------------------------------------

number = "12345"

print(number.isdigit())


# ------------------------------------------------------------
# 30. String Methods - isalnum()
# ------------------------------------------------------------

text = "Python123"

print(text.isalnum())


# ------------------------------------------------------------
# 31. String Methods - isspace()
# ------------------------------------------------------------

text = "   "

print(text.isspace())


# ------------------------------------------------------------
# 32. String Methods - swapcase()
# ------------------------------------------------------------

text = "Python Programming"

print(text.swapcase())


# ------------------------------------------------------------
# 33. String Methods - center()
# ------------------------------------------------------------

text = "Python"

print(text.center(20, "-"))


# ------------------------------------------------------------
# 34. String Methods - zfill()
# ------------------------------------------------------------

number = "42"

print(number.zfill(5))


# ------------------------------------------------------------
# 35. String Formatting With Variables
# ------------------------------------------------------------

name = "Aayushman"
course = "Data Science"
year = 2026

profile = f"""
Name: {name}
Course: {course}
Year: {year}
"""

print(profile)


# ------------------------------------------------------------
# 36. Practical Example
# ------------------------------------------------------------

first_name = "Aayushman"
last_name = "Baruah"

full_name = f"{first_name} {last_name}"

bio = "  Python Developer and Data Science Learner  "

clean_bio = bio.strip()

print("Full Name:", full_name)
print("Bio:", clean_bio)
print("Name Length:", len(full_name))
print("Uppercase:", full_name.upper())
print("Lowercase:", full_name.lower())
print("Contains Python:", "Python" in clean_bio)


# ============================================================
# KEY TAKEAWAYS
# ============================================================
#
# 1. A string is a sequence of characters.
#
# 2. Strings can be created using single or double quotes.
#
#    "Hello"
#    'Hello'
#
# 3. Triple quotes can be used for multiline strings.
#
# 4. Strings are indexed starting from 0.
#
#    "Python"
#     012345
#
# 5. Negative indexing starts from the end.
#
#    "Python"
#     -6 -5 -4 -3 -2 -1
#
# 6. Use len() to find the length of a string.
#
# 7. Use slicing to extract part of a string.
#
#    text[start:end]
#
# 8. Use in and not in to check whether text exists.
#
# 9. Strings are immutable.
#    String methods return a new string instead of changing
#    the original string.
#
# 10. Important string modification methods:
#
#     upper()
#     lower()
#     strip()
#     replace()
#     split()
#     capitalize()
#     title()
#
# 11. String concatenation combines strings using +.
#
# 12. join() can combine multiple strings into one string.
#
# 13. Escape characters allow special characters inside strings.
#
#     \n  -> new line
#     \t  -> tab
#     \\  -> backslash
#     \"  -> double quote
#
# 14. f-strings are the preferred way to insert variables
#     and expressions into strings.
#
#     f"Hello {name}"
#
# 15. Python provides many built-in string methods for
#     searching, checking, modifying, and formatting text.
#
# 16. Strings are extremely important in real-world Python
#     because text data appears everywhere:
#
#     - User input
#     - CSV files
#     - Databases
#     - APIs
#     - Web scraping
#     - Natural Language Processing
#     - Machine Learning datasets
#
# ============================================================