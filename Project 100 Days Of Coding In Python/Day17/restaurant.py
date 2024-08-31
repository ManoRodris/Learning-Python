class Restaurant:

    def __init__(self, name_of_restaurant, type_of_restaurant):
        self.restaurant = name_of_restaurant
        self.type = type_of_restaurant
        self.customer = 0

    def describe_restaurant(self):
        print(f"Name: {self.restaurant}")
        print(f"Type of restaurant: {self.type}")

    def open_restaurant(self):
        print(f"The {self.restaurant} is open!")

    def amount_of_customers(self):
        print(f"The current amount of customers: {self.customer}")

    def change_customers(self, customers):
        self.customer = customers