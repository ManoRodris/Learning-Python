from restaurant import Restaurant

class IceCreamStand(Restaurant):
    def __init__(self, name_of_restaurant, type_of_restaurant):
        super().__init__(name_of_restaurant, type_of_restaurant)
        self.flavors = ["vanilla", "chocolate", "passion fruit"]

    def show_flavors(self):
        for flav in self.flavors:
            print("We has " + flav + " ice cream in our menu")

restaurant_1 = Restaurant("Gousteau", "French cuisine")
restaurant_2 = Restaurant("Nildo", "Self service")
restaurant_3 = Restaurant("The Bear","Homemade food")

# restaurants = [restaurant_1, restaurant_2, restaurant_3]
#
# for res in restaurants:
#     res.describe_restaurant()
#     res.open_restaurant()
#     print("\n")

# restaurant_1.amount_of_customers()
# restaurant_1.customer = 2
# print("\n")
# restaurant_1.amount_of_customers()

# restaurant_2.amount_of_customers()
# restaurant_2.change_customers(7)
# print("\n")
# restaurant_2.amount_of_customers()

ice_cream_shop = IceCreamStand("Cold kiss", "Ice cream shop")
ice_cream_shop.show_flavors()