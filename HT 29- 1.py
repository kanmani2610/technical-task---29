class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, title, quantity):
        self.books[title] = self.books.get(title, 0) + quantity

    def display_books(self):
        return self.books


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, title):
        self.borrowed_books.append(title)


class LibraryManagement(Library, Member):
    def __init__(self, name):
        Library.__init__(self)
        Member.__init__(self, name)

    def borrow(self, title):
        if self.books.get(title, 0) > 0:
            self.borrow_book(title)
            self.books[title] -= 1
            return f"{title} borrowed."
        return f"{title} not available."
system = LibraryManagement("John")
system.add_book("Python Programming", 5)
print(system.display_books())  # {'Python Programming': 5}
print(system.borrow("Python Programming"))  # Python Programming borrowed.
print(system.display_books())  # {'Python Programming': 4}
