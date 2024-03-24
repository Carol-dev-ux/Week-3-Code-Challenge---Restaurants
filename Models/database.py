import sqlite3
from restaurant import Restaurant
from customer import Customer
from review import Review

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_tables(self):
        try:
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS restaurants (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    price INTEGER
                )
            ''')

            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS customers (
                    id INTEGER PRIMARY KEY,
                    first_name TEXT,
                    last_name TEXT
                )
            ''')

            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS reviews (
                    id INTEGER PRIMARY KEY,
                    restaurant_id INTEGER,
                    customer_id INTEGER,
                    star_rating INTEGER,
                    FOREIGN KEY (restaurant_id) REFERENCES restaurants(id),
                    FOREIGN KEY (customer_id) REFERENCES customers(id)
                )
            ''')

            self.conn.commit()
            print("Tables created successfully!")
        except sqlite3.Error as e:
            print("An error occurred:", e)