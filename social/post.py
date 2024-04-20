from datetime import datetime

class Post:

    entries = list()

    def __init__(self):
        self.author = input("Enter nickname: ")
        self.text = input("Write your post: ")
        self.created_at = datetime.now()
        self.entries.append(self)
        self.id = len(self.entries)

    def __str__(self):
        return f"#{self.id} {self.author} said: {self.text}"