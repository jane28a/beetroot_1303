from post import Post

if __name__ == "__main__":
    while True:
        print("Welcome to the new social")
        message = ("""
            Choose the option:
            1. Add post
            2. See all posts
            3. Like post
            4. Dislike post
            0. Exit 

            Your Choice: """)
        choice = input(message)
        match choice:
            case "1":
                Post()
            case "2":
                Post.show_posts()
            case "3":
                Post.like()
            case "4":
                Post.dislike()
            case "0":
                break
            case _:
                print("Wrong choice")
