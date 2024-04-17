class Book:
    
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        pages = input("How many pages: ")
        if pages:
            self.pages = pages
        else:
            self.pages = None
        
    def print(self):
        print(f"This is {self.title} by {self.author} and has {self.pages} pages")

if __name__ == "__main__":
    book = Book(
        "Dune", "Herbert", "Science fiction"
    )
    print(book)
    book.print() # Book.print(book)
    book.location = "library"
