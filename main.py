from Models.customer import Customer 
from Models.database import Database  
from Models.restaurant import Restaurant
from Models.review import Review  

def main():
    # Initialize the database
    db = Database('restaurant_reviews.db')
    db.create_tables()  

    # Create some sample instances
    restaurant1 = Restaurant(1, "Restaurant A", 20)
    restaurant2 = Restaurant(2, "Restaurant B", 30)
    customer1 = Customer(1, "John", "Doe")
    customer2 = Customer(2, "Jane", "Smith")

    # Add some reviews
    customer1.add_review(restaurant1, 5)
    customer2.add_review(restaurant1, 4)
    customer2.add_review(restaurant2, 3)

    # Test methods
    print("Customer full name:", customer1.full_name())
    print("Customer favorite restaurant:", customer2.favorite_restaurant().name if customer2.favorite_restaurant() else "None")
    print("All reviews by customer2:")
    for review in customer2.reviews():
        print(review.full_review())

    print("All reviews for restaurant1:")
    for review in restaurant1.reviews():
        print(review.full_review())

    print("All customers who reviewed restaurant1:")
    for customer in restaurant1.customers():
        print(customer.full_name())

    print("All reviews for restaurant1 formatted:")
    print(restaurant1.all_reviews())

if __name__ == "__main__":
    main()
