import sqlite3
from customer import Customer
from restaurant import Restaurant
from database import Database


class Review:
    def __init__(self, review_id, restaurant_id, customer_id, star_rating):
        self.review_id = review_id
        self.restaurant_id = restaurant_id
        self.customer_id = customer_id
        self.star_rating = star_rating

    def customer(self):
        # Fetch Customer instance for this review from the database
        db = Database('your_database_name.db')
        db.cursor.execute('SELECT * FROM customers WHERE id = ?', (self.customer_id,))
        customer_data = db.cursor.fetchone()
        if customer_data:
            customer_instance = Customer(*customer_data)
            return customer_instance
        else:
            return None

    def restaurant(self):
        # Fetch Restaurant instance for this review from the database
        db = Database('your_database_name.db')
        db.cursor.execute('SELECT * FROM restaurants WHERE id = ?', (self.restaurant_id,))
        restaurant_data = db.cursor.fetchone()
        if restaurant_data:
            restaurant_instance = Restaurant(*restaurant_data)
            return restaurant_instance
        else:
            return None

    def full_review(self):
        # Fetch restaurant name and customer's full name and format the review string
        customer_instance = self.customer()
        restaurant_instance = self.restaurant()
        if customer_instance and restaurant_instance:
            return f"Review for {restaurant_instance.name} by {customer_instance.full_name()}: {self.star_rating} stars."
        else:
            return "Review details unavailable due to missing data."




