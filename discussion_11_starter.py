import unittest
import sqlite3
import json
import os


# Create Database
def set_up_database(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path + "/" + db_name)
    cur = conn.cursor()
    return cur, conn


# Creates list of species ID's and numbers
def create_species_table(cur, conn):
    species = [
        "Rabbit",
        "Dog",
        "Cat",
        "Boa Constrictor",
        "Chinchilla",
        "Hamster",
        "Cobra",
        "Parrot",
        "Shark",
        "Goldfish",
        "Gerbil",
        "Llama",
        "Hare",
    ]

    cur.execute("DROP TABLE IF EXISTS Species")
    cur.execute("CREATE TABLE Species (id INTEGER PRIMARY KEY, title TEXT)")
    for i in range(len(species)):
        cur.execute("INSERT INTO Species (id,title) VALUES (?,?)", (i, species[i]))
    conn.commit()


# TASK 1
# Create table for Patients in SQLite Database
def create_patients_table(cur, conn):
    pass


# Function to add Sprinkles to the table
def add_sprinkles(cur, conn):
    pass


# TASK 2
# Function to add DownTheStreet's patient list to your own. For this function assume the table exists
def add_pets_from_json(filename, cur, conn):
    # We've given you this to read in the data from the provided JSON file.
    f = open(filename)
    file_data = f.read()
    f.close()
    json_data = json.loads(file_data)

    # Complete the rest of this function
    pass

# TASK 3
# Function to find non aggressive pets for the intern
def non_aggressive_pets(aggressiveness, cur, conn):
    pass


class TestAllMethods(unittest.TestCase):
    def setUp(self):
        self.cur, self.conn = set_up_database("animal_hospital.db")
        create_species_table(self.cur, self.conn)

    def tearDown(self):
        # Closes the database connection after each test
        self.conn.close()

    def test_1_create_patients_table(self):
        create_patients_table(self.cur, self.conn)
        self.conn.commit()
        self.cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
        results = self.cur.fetchall()
        self.assertEqual(results[1], ("Patients",))

    def test_2_add_sprinkles(self):
        add_sprinkles(self.cur, self.conn)
        self.cur.execute("SELECT age, cuteness FROM Patients WHERE name='Sprinkles'")
        result = self.cur.fetchone()
        self.assertEqual(result, (2, 99))

    def test_3_add_pets_from_json(self):
        add_pets_from_json("pets.json", self.cur, self.conn)
        self.cur.execute("SELECT name FROM Patients WHERE name <> 'Sprinkles'")
        results = self.cur.fetchall()
        self.assertEqual(len(results), 11)

    def test_4_non_aggressive_pets(self):
        list_of_pets = non_aggressive_pets(10, self.cur, self.conn)
        self.assertEqual(
            list_of_pets,
            [
                "Barky",
                "Cupid",
                "King FluffyPaw The Righteous",
                "Queen Mittens The Benevolent",
                "Prince BigTail The Clueless",
                "FluFlea",
                "Sash",
            ],
        )


def main():
    pass


if __name__ == "__main__":
    main()
    unittest.main(verbosity=2)
