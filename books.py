import datetime
import json

BOOKS = [
    {
        "name": "Dune",
        "author": "Frank Herbert",
        "genre": "Science fiction",
        "pages": 896,
        # "entry_added": datetime.datetime(2023, 11, 15, 12, 13, 14),
    },
    {
        "name": "Dune Messiah",
        "author": "Frank Herbert",
        "genre": "Science fiction",
        "pages": 256,
        # "entry_added": datetime.datetime(2023, 12, 16, 20, 0, 11),
    },
    {
        "name": "Murder on the Orient Express",
        "author": " Agatha Christie",
        "genre": "Crime novel",
        "pages": 256,
        # "entry_added": datetime.datetime(2021, 10, 30, 7, 43, 28),
    },
]

if __name__ == "__main__":
    with open("books.json", "w") as data_file:
        json.dump(BOOKS, data_file, skipkeys=True)





