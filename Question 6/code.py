# Question 6
"""A school administration system uses a Python program to
manage student records using file handling.
When a new academic session starts, the system creates a
text file named students.txt to store student details
such as roll number, name, and class.
The administrator enters student information,
and the program opens the file in write mode
to save these details permanently.
Whenever the administrator wants to view the stored records,
the file is opened in read mode,
and all student data is displayed on the screen.
If new students are admitted later, the program opens
the same file in append mode so that new records
are added without deleting the existing data."""

# Source code

# Starting new session
st_name = input("Enter student name: ")
st_class = input("Enter student class: ")
st_roll = input("Enter student roll no: ")
record = f"Student Name: {st_name}, Class: {st_class}, Section: {st_roll}\n"

file = open("students.txt", "w")
file.write(record)
file.close()

# Viewing the reocrd
file = open("students.txt", "r")
print("Saved records:")
f_record = file.readline()
while(f_record):
    print(f_record)
    f_record = file.readline()
file.close()

# Adding a new student later on
print("Adding a new student later:")
st_name = input("Enter student name: ")
st_class = input("Enter student class: ")
st_roll = input("Enter student roll no: ")
record = f"Student Name: {st_name}, Class: {st_class}, Section: {st_roll}\n"

file = open("students.txt", "a")
file.write(record)
file.close()