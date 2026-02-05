# Required modules to import
import random

# Question 4
"""A school is organizing a fun quiz competition and wants to
select students randomly for different activities.
The Python program uses the random module to
make selections fair and unpredictable.
First, the teacher enters the names of all participating students.
The system uses random.choice() to
select a single student randomly to answer a question.
To randomize the order of students for games or presentations,
the program uses random.shuffle() on the list of student names.
For some mini-games, the system generates random numbers using
random.randint() to simulate dice rolls or points scoring.
This ensures the quiz and games are exciting, fair, and unpredictable,
giving every student an equal chance to participate."""

# Source code

# Teacher entering student names
no_of_students = int(input("Enter no of students: "))
students = []
for i in range(no_of_students):
    std_name = input(f"Enter student {i+1} name: ")
    students.append(std_name)

# Selecting a random student
selected_student = random.choice(students)
print(f"{selected_student} is randomly selected to answer a question")

# Randommizing order of students
random.shuffle(students)
print("Students order after re-shuffle:")
for i, name in enumerate(students):
    print(f"{i}: {name}")
    
# Selecting a random dice score
dice_value = random.randint(1,6)
print(f"Randomly selected dice value is: {dice_value}")

# Selecting a random score
score = random.randint(0, 10)
print(f"Random score between 0 to 10: {score}")