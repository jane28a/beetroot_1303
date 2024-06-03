import sqlite3

connection = sqlite3.connect("person.db")
cursor = connection.cursor()

class Person:

    def __init__(self, _id, name, age):
        self.id = _id
        self.name = name
        self.age = age

if __name__ == "__main__":
#    cursor.execute("""
#        CREATE TABLE IF NOT EXISTS person(
#            id INTEGER PRIMARY KEY,
#            name CHAR(30),
#            age INTEGER
#        )
#    """)
#    cursor.execute("""
#        INSERT INTO person VALUES
#        (1, "Vasya", 15),
#        (2, "Petro", 80)
#    """)
#    connection.commit()

#    persons = cursor.execute("""
#        SELECT DISTINCT name FROM person
#    """)
#    unique_names = {person[0] for person in persons.fetchall()}
#    print(unique_names)
#    for person in persons.fetchall():
#        print(person)
#    cursor.execute("""
#        UPDATE person
#        SET age = 16
#        WHERE name = "Vasya"
#    """)
#    connection.commit()
#    persons = cursor.execute("""
#        SELECT * FROM person
#    """)
#    for person in persons.fetchall():
#        print(person)
#    cursor.execute("""DROP TABLE person""")
#    connection.commit()