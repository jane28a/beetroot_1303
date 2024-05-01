import json
import csv

if __name__ == "__main__":

    with open("books.json", "r") as json_file, open("books.csv", "w") as csv_file:
        data = json.load(json_file)
        writer = csv.writer(csv_file)
        for book in data:
            writer.writerow(book)
