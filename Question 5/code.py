# Question 5
"""A college wants to manage and format
its course information using a Python program.
The system allows the user to enter the course name and
department name and displays them in a readable format.
The program applies the title() function to the course name
so that the first letter of each word is capitalized,
and the capitalize() function to the department name to
ensure only the first letter is uppercase.
If the course name contains a mistake, the program allows the user
to enter an old name and a new name, and uses the replace() 
function to update the course name.
Additionally, the program extracts specific parts of the course name
using string slicing with index values: the first two characters
(index 0 to 1) are extracted as the course code,
characters from index 1 to 4 are extracted as a verification part,
and the last three characters (using negative indexing, -3 to end)
are extracted as the course ID.
Finally, the program displays the updated course name
along with the course code, course ID, and verification part."""


# Source code
course_name = input("Enter course name: ")
depart_name = input("Enter department name: ")

# Case changes as required
course_name = course_name.title()
depart_name = depart_name.capitalize()

# Displaying info
print(f"Course Name: {course_name}")
print(f"Department Name: {depart_name}")

# Updating wrong course name
old_name = input("Enter old course name: ")
new_name = input("Enter new course name: ")
course_name = course_name.replace(old_name, new_name)

# Specific parts of course name
course_code = course_name[0:2]
verification_part = course_name[1:5]
course_id = course_name[-3:]

# Printing updated informations
print(f"Updated Course Name: {course_name}")
print(f"Course Code: {course_code}")
print(f"Course ID: {course_id}")
print(f"Verification Part: {verification_part}")