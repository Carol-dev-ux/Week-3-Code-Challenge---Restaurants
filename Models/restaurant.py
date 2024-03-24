from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .Base import Base

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    reviews = relationship('Review', back_populates='restaurant')

    def customers(self):
        return [review.customer for review in self.reviews]

    @classmethod
    def fanciest(cls, session):
        fanciest_restaurant = session.query(cls).order_by(cls.price.desc()).first()
        return fanciest_restaurant

    def all_reviews(self):
        return [f"Review for {self.name} by {review.customer.full_name()}: {review.star_rating} stars." for review in self.reviews]

    def __repr__(self):
        return f"<Restaurant(id={self.id}, name='{self.name}', price={self.price})>"
