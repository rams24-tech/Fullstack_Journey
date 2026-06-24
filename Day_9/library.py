class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author

    def __str__(self):
        return(f"{self.title} by {self.author}")

class Library:
    def __init__(self,name):
        self.name=name
        self.books=[]

    def add_book(self,book):
        self.book=book
        self.books.append(book)
        print(f"{book.title} added to {self.name} ")

    def show_books(self):
        print(f"{self.name} has:")
        for i in self.books:
            print(f"- {str(i)}")    

    def find_book(self,title):
        x=0
        for i in self.books:
            if i.title==title:
                print(f"Found: {str(i)}")
                x=x+1
        if x==0:
            print("Book not found")    
lib = Library("City Library")

b1 = Book("The Alchemist", "Paulo Coelho")
b2 = Book("Atomic Habits", "James Clear")
b3 = Book("Deep Work", "Cal Newport")

lib.add_book(b1)
lib.add_book(b2)
lib.add_book(b3)

lib.show_books()
lib.find_book("Atomic Habits")
lib.find_book("Harry Potter")