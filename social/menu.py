from post import Post

if __name__ == "__main__":
    while True:
        print("Welcome to the new social")
        message = ("""
            Choose the option:
            1. Add post
            2. See all posts
            0. Exit 

            Your Choice: """)
        choice = input(message)
        match choice:
            case "1":
                new_post = Post()
            case "2":
                for entry in Post.entries:
                    print(entry)
            case "0":
                break
            case _:
                print("Wrong choice")
