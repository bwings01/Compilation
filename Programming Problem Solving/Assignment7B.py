class Book:

    # attributes
    def __init__(self, title):
        self.title = title
        self.is_borrowed = False

    # method for borrowing
    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f'You borrowed "{self.title}".')
        else:
            print(f'Error: "{self.title}" is already borrowed.')

    # method for returning
    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f'You returned "{self.title}".')
        else:
            print(f'Error: "{self.title}" was not borrowed.')
            
    # method for displaying info
    def display_info(self, index):
        status = "Available" if not self.is_borrowed else "Borrowed"
        print(f"{index} - {self.title} ({status})")


class Library:

    # attributes
    def __init__(self):
        # list of Book objects, as required
        self.books = [
            Book("Python Basics"),
            Book("Intro to AI")
        ]
    
    # method for showing books
    def show_books(self):
        print("Books in Library:")
        for i, book in enumerate(self.books):
            book.display_info(i)
    
    # method for borrowing book
    def borrow_book(self):
        try:
            self.show_books()
            index = int(input("Select a book to borrow: "))
            if 0 <= index < len(self.books):
                book = self.books[index]
                book.borrow()
            else:
                print("Error: Invalid book number.")
        except ValueError:
            print("Error: Please enter a valid number.")
    
    # method for returning book
    def return_book(self):
        try:
            self.show_books()
            index = int(input("Select a book to return: "))
            if 0 <= index < len(self.books):
                book = self.books[index]
                book.return_book()
            else:
                print("Error: Invalid book number.")
        except ValueError:
            print("Error: Please enter a valid number.")

    # method for adding book
    def add_book(self):
        title = input("Enter the title of the new book: ")
        new_book = Book(title)
        self.books.append(new_book)
        print(f'"{title}" has been added to the library!')


def main():
    library = Library()
    while True:
        print("[Owl Library]")
        print("1. View Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Add Book")
        print("5. Exit")
        try:
            choice = int(input("> "))
            if choice == 1:
                library.show_books()
            elif choice == 2:
                library.borrow_book()
            elif choice == 3:
                library.return_book()
            elif choice == 4:
                library.add_book()
            elif choice == 5:
                print("Exiting program... Goodbye!")
                break
            else:
                print("Error: Please select a number between 1 and 5.")
        except ValueError:
            print("Error: Please enter a valid number.")


if __name__ == "__main__":
    main()
