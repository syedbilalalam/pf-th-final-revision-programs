# Question 8
"""A student marks system ensures that
the marks entered are valid (between 0 and 100).
If the user enters invalid marks,
the program stops immediately using assert"""


# Source code
marks = int(input("Enter student marks (0-100): "))

# Assert condition to validate marks
assert marks>=0 and marks<=100, "Invalid marks! Marks must be between 0 and 100."

print(f"Marks entered successfully: {marks}")
print("Marks are valid and accepted.")