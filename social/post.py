from datetime import datetime

class Content:
    
    def __init__(self):
        self.author = input("Enter nickname: ")
        self.text = input("Write your post: ")
        self.created_at = datetime.now()

    def __str__(self):
        return f"{self.author} said at {self.created_at}: {self.text}"

class Post(Content):

    entries = list()

    def __init__(self):
        super().__init__() # Content.__init__()
        self.entries.append(self)
        self.id = len(self.entries)
        self.likes = 0

    def __str__(self):
        return (f"#{self.id} {self.author} said: {self.text}. "
            + f"Likes: {self.likes}")

    @classmethod
    def like(cls):
        post_id = input("Enter post id: ")
        for post in cls.entries:
            if post.id == int(post_id):
                post.likes += 1
                break
        
class Comment(Content):

    def __init__(self, post_id):
        super().__init__()
        self.post_id = post_id

    def __str__(self):
        return f"{self.author} commented on {self.post_id}: {self.text}" 

if __name__ == "__main__":

    comment1 = Comment(1)
    comment2 = Comment(1)
    del comment1.author
    comment2.note = "some note"
    print(comment2)
    print(comment1)
