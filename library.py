import random
print("Wlecome to my library")
def library():
    print("What do you want to do? ")
    menu = input("1. Add a new boook 2. Delete a book 3. List all books 4. Exit the library 5. To edit book: ")
    
    if menu == "1":
        new_library.add_book()
    elif menu == "2":
        new_library.remove_book()
    elif menu == "3":
        new_library.list_all_books()
    elif menu == "4":
        print("byE!!! hope to see you again.")
        return
    elif menu == "5":
        new_library.edit_book()
    else: 
        print("Invalid entry.")

    print("Would you like to do anything else? ")
    go_back = input("1. Yes 2. No: ")
    if go_back == "1":
        library()
    else:
        print("Thanks for your time.")

class Book:
    def __init__(self):
        self.title = input("Enter the title of the book: ")
        self.author = input("Enter the author of the book: ")
        self.pages = int(input("Enter the number of pages of the book: "))
        self.isbn = random.randint(1000000, 100000000)
        print(f"{self.title} added successfully")


    def edit_book(self):
        new_title = input("Enter the new title: ")
        self.title = new_title
        print("Book edited successfully.")



class Library:
    def __init__(self):
        self.all_books = {}

    def add_book(self):
        new_book = Book()
        isbn = new_book.isbn 
        self.all_books[isbn] = new_book
        print(f"{new_book.title} added to the dictionary successfully.")
        
    def remove_book(self):
        isbn = int(input("Enter the book's ISBN: "))
        about_to_be_removed = self.all_books[isbn]
        del self.all_books[isbn]
        print(f"{about_to_be_removed.title} has been removed")

    def list_all_books(self):
        for key, value in self.all_books.items():
            print(f"ISBN: {key}, Title: {value.title}")

    def edit_book(self):
        isbn = int(input("Enter the ISBN of the book: "))
        edited_book = self.all_books[isbn]
        edited_book.edit_book()

new_library = Library()
library()


