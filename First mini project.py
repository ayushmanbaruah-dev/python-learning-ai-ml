# ============================================================
# 06_student_score_calculator.py
# Student Score Calculator
#
# Description:
# A simple Python program that calculates a student's
# total marks, average marks, and pass/fail status.
#
# Concepts Used:
# - Variables
# - Data types
# - Arithmetic operators
# - Comparison operators
# - Boolean values
#
# ============================================================
# 1. Create student information
# 2. Store marks
# 3. Calculate total
# 4. Calculate average
# 5. Determine pass/fail
# 6. Display results


# ============================================================
# 06_student_score_calculator.py
# Student Score Calculator
#
# Description:
# A simple Python program that calculates a student's
# total marks, average marks, and pass/fail status.
#
# Concepts Used:
# - Variables
# - Data types
# - Arithmetic operators
# - Comparison operators
# - Boolean values
# - f-strings
#
# ============================================================


# ------------------------------------------------------------
# 1. Student Information
# ------------------------------------------------------------

student_name = "Aayushman"


# ------------------------------------------------------------
# 2. Subject Marks
# ------------------------------------------------------------

python_marks = 85
sql_marks = 78
math_marks = 92


# ------------------------------------------------------------
# 3. Calculate Total Marks
# ------------------------------------------------------------

total_marks = python_marks + sql_marks + math_marks


# ------------------------------------------------------------
# 4. Calculate Average Marks
# ------------------------------------------------------------

average_marks = total_marks / 3


# ------------------------------------------------------------
# 5. Determine Pass/Fail
# ------------------------------------------------------------

passed = average_marks >= 40


# ------------------------------------------------------------
# 6. Display Results
# ------------------------------------------------------------

print(f"Student: {student_name}")
print(f"Python: {python_marks}")
print(f"SQL: {sql_marks}")
print(f"Math: {math_marks}")

print(f"Total: {total_marks}")
print(f"Average: {average_marks}")
print(f"Passed: {passed}")


# ============================================================
# KEY TAKEAWAYS
# ============================================================
#
# 1. Think about the problem before writing code.
#
# 2. Break a problem into smaller steps.
#
# 3. Use the Input → Process → Output model.
#
# 4. Use descriptive variable names.
#
# 5. Arithmetic operators can be used to calculate values.
#
# 6. Comparison operators return True or False.
#
# 7. f-strings make it easy to display variables inside text.
#
# 8. Comments can document what different parts of the
#    program are doing.
#
# 9. A good programmer doesn't try to solve the whole
#    problem at once. They build and test one piece at a time.
#
# ============================================================