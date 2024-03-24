 # Customer.py
from sqlalchemy import Column, Integer, String, ForeignKey, func
from sqlalchemy.orm import relationship
from .Base import Base

# Import Reviews and Restaurant classes here to avoid circular imports
from .Reviews import Reviews
from .Restaurant import Restaurant

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    reviews = relationship('Reviews', back_populates='customer')

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    # Object Relationship Methods
    def get_reviews(self):
        return self.reviews

    def restaurants(self):
        return [review.restaurant for review in self.reviews]

    # Aggregate and Relationship Methods
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def favorite_restaurant(self, session):
        return session.query(Restaurant).join(Reviews).filter(Reviews.customer_id == self.id).order_by(Reviews.star_rating.desc()).first()

    def add_review(self, session, restaurant, rating):
        new_review = Reviews(customer=self, restaurant=restaurant, star_rating=rating)
        session.add(new_review)
        session.commit()

    def delete_reviews(self, session, restaurant):
        session.query(Reviews).filter(Reviews.customer_id == self.id, Reviews.restaurant_id == restaurant.id).delete()
        session.commit()
     




