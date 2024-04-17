class Book:
    
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        
    def print(self):
        print(f"This is {self.title} by {self.author}")

if __name__ == "__main__":
    book = Book(
        "Dune", "Herbert", "Science fiction"
    )
    print(book)
    book.print() # Book.print(book)