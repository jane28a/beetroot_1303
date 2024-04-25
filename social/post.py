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
        self.dislikes = 0

    def __str__(self):
        return (f"#{self.id} {self.author} said: {self.text}. "
            + f"Likes: {self.likes} | Dislikes: {self.dislikes}")

    def __eq__(self, other):
        return self.rating == other.rating

    @classmethod
    def show_posts(cls):
        for entry in sorted(cls.entries, reverse=True):
            print(entry)

    def get_rating(post):
        return post.rating

    @classmethod
    def find_by_id(cls):
        post_id = input("Enter post id: ")
        for post in cls.entries:
            if post.id == int(post_id):
                return post

    @classmethod
    def like(cls):
        post = cls.find_by_id()
        post.likes += 1

    @classmethod
    def dislike(cls):
        post = cls.find_by_id()
        post.dislikes += 1

    @property
    def rating(self):
        return self.likes - self.dislikes
        
class Comment(Content):

    def __init__(self, post_id):
        super().__init__()
        self.post_id = post_id

    def __str__(self):
        return f"{self.author} commented on {self.post_id}: {self.text}" 

if __name__ == "__main__":

    post1 = Post() # rating 1
    post2 = Post() # rating -1
    Post.like(1)
    Post.dislike(2)
    print(post1 == post2)

