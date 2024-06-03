import sqlite3
from sqlite3 import IntegrityError as BigError
from contextlib import closing

def write_to_db(cursor, name, age):
    data = {"name": name, "age": age}
    cursor.execute("""
        INSERT INTO person(name, age) VALUES(:name, :age)
    """, data)


class Person:

    def __init__(self, _id, name, age):
        self.id = _id
        self.name = name
        self.age = age

if __name__ == "__main__":
    with closing(sqlite3.connect("person.db")) as connection:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS person(
                person_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name CHAR(30) UNIQUE,
                age INTEGER
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS contacts(
                owner_id INTEGER UNIQUE NOT NULL,
                contact_id INTEGER PRIMARY KEY,
                type CHAR(16),
                value CHAR(50),
                FOREIGN KEY (owner_id)
                    REFERENCES person (person_id)

            )
        """)

#        id = """SELECT id FROM person WHERE name = 'Vasya'"""
#        contacts = """SELECT type, value FROM contacts WHERE owner_id = id"""

        try:
            with connection:
                write_to_db(cursor, "Mariia Ivanivna", 58)
                write_to_db(cursor, "Vasya", 15)
                write_to_db(cursor, "Petro", 72)
        except BigError:
            pass

        persons = cursor.execute("""
            SELECT DISTINCT name FROM person
        """)

#        unique_names = {person[0] for person in persons.fetchall()}
#        print(unique_names)
        for person in persons.fetchall():
            print(person)

        try:
            cursor.execute("""
                UPDATE person
                SET age = 16
                WHERE name = "Vasya"
            """)
            connection.commit()
        except:
            connection.roll_back()

#        cursor.execute("""DROP TABLE person""")
#        connection.commit()