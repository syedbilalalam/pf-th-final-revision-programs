# Question No 1
"""Write a program that simulates how websites ensure that everyone has a unique username.
Make a list of five or more usernames called current_users.
Make another list of five usernames called new_users.
Make sure one or two of the new usernames are also in the current_users list.
Loop through the new_users list to see if each new username has already been used.
If it has, print a message that the person will need to enter a new username.
If a username has not been used, print a message saying that the username is available.
Make sure your comparison is case sensitive.
If 'John' has been used, 'JOHN' should not be accepted.
(To do this, you'll need to make a copy of current_users containing the
lowercase versions of all existing users)."""

# Source Code
current_users = ["Bilal", "Ahmed", "Saad", "Haris", "Jhon"]
new_users = ["BILAL", "Sheikh", "Haris", "Jawwad", "Hunain"]

current_users_lowered = [username.lower() for username in current_users]

for new_username in new_users:
    if new_username.lower() in current_users_lowered:
        print(f"{new_username} is already taken!")
    else:
        print(f"{new_username} is available")
