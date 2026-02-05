# Question 3
"""A college library maintains a record of book ID numbers
using a tuple in Python to keep the data secure and unchanged by default.
First, the librarian enters the total number of books and inputs each book ID,
and the system stores these values in a tuple and displays the original list
along with their index positions. Since tuples are immutable,
the program converts the tuple into a list to perform modifications.
When new books arrive, a new book ID is inserted at a specific index
position (for example, index 2), and the system displays the updated tuple
along with the index where the insertion occurred.
If some books are removed due to damage or outdated editions, a book ID
is deleted from a given index position (such as index 4),
and the system shows the updated tuple and the index from which the value
was removed. Additionally, if an incorrect book ID is detected,
the librarian updates the book ID at a particular index (for example, index 1),
and the program displays the modified tuple while clearly mentioning
the index where the updation took place.
This approach helps the library manage book records efficiently
while keeping track of all changes using index values."""


# Source Code
no_of_books = int(input("Enter no of books: "))
book_ids_list = []
for i in range(no_of_books):
    input_id = int(input(f"Enter book {i+1} id: "))
    book_ids_list.append(input_id)

book_ids = tuple(book_ids_list)

# Display Original List
print("Original List:")
for i in range(len(book_ids)):
    print(f"Index:{i} => Id: {book_ids[i]}")

# New book addition
new_book_id = int(input("Enter new book id: "))
book_ids_list.insert(2, new_book_id)
book_ids = tuple(book_ids_list)

# Display Updated Tuple
print("Tuple after new books addition:")
for i, book_id in enumerate(book_ids):
    print(f"Index:{i} => Id: {book_id}")
    
# Removing at specific index
try:
    book_ids_list.pop(4)
    book_ids = tuple(book_ids_list)
    
    # Display Updated Tuple
    print("Tuple after old books deletion:")
    for i, book_id in enumerate(book_ids):
        print(f"Index:{i} => Id: {book_id}")

except:
    print("List doesn't have 4th index to remove")

# Updating invalid book id
incorrect_index = 1
correct_book_id = int(input("Enter correct book id: "))
try:
    book_ids_list[incorrect_index] = correct_book_id
    book_ids = tuple(book_ids_list)

    # Display Updated Tuple
    print("After updating invalid book id:")
    for i, book_id in enumerate(book_ids):
        print(f"Index:{i} => Id: {book_id}")
except:
    print("Index does not exists to update the book id")




