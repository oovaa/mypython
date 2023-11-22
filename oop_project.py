from typing import List


class Book:
    def __init__(self):
        self.title = ""
        self.author = ""
        self.ISBN = ""
        self.isChecked = False

    def getTitle(self) -> str:
        return self.title

    def getAuthor(self) -> str:
        return self.author

    def getISBN(self) -> str:
        return self.ISBN

    def __str__(self) -> str:
        return self.title

    def displat_info(self):
        string = "title: {}\nAuthor: {}\nISBN: {}".format(
            self.title, self.author, self.ISBN
        )
        print(string)


class Members:
    def __init__(self):
        self.mem_id = ""
        self.name = ""
        self.checked_out = []

    def check_out_book(self, book: Book):
        book.isChecked = True
        self.checked_out.append(book)

    def return_book(self, book: Book):
        self.checked_out.remove(book)

    def __str__(self) -> str:
        return self.name

    def display_info(self):
        checked_out_books = [book.title for book in self.checked_out]
        string = "mem_id: {}\nname: {}\nchecked_out: {}".format(
            self.mem_id, self.name, checked_out_books
        )
        print(string)


class Library:
    def __init__(self) -> None:
        self.books: List(Book) = []
        self.members: List(Members) = []

    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book(self, book: Book):
        self.books.remove(book)

    def add_member(self, member: Members):
        self.members.append(member)

    def remove_member(self, member: Members):
        self.members.remove(member)

    def displat_Books(self):
        books_names = [book.title for book in self.books]
        print(books_names)

    def displat_members(self):
        memnames = [mem.name for mem in self.members]
        print(memnames)


if __name__ == "__main__":
    # Create some book instances
    book1 = Book()
    book1.title = "The Catcher in the Rye"
    book1.author = "J.D. Salinger"
    book1.ISBN = "978-0-316-76948-0"

    book2 = Book()
    book2.title = "To Kill a Mockingbird"
    book2.author = "Harper Lee"
    book2.ISBN = "978-0-06-112008-4"

    # Create some member instances
    member1 = Members()
    member1.mem_id = "001"
    member1.name = "John Doe"

    member2 = Members()
    member2.mem_id = "002"
    member2.name = "Jane Doe"

    # Create a library instance
    library = Library()

    # Add books and members to the library
    library.add_book(book1)
    library.add_book(book2)

    library.add_member(member1)
    library.add_member(member2)

    # Display books and members
    print("Books in the library:")
    library.displat_Books()

    print("\nMembers in the library:")
    library.displat_members()

    # Check out a book and display member info
    member1.check_out_book(book1)
    print("\nAfter checking out a book:")
    member1.display_info()
