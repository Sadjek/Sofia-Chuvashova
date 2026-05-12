class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Название ресторана: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")

    def open_restaurant(self):
        print("Ресторан открыт!")


newRestaurant1 = Restaurant ("ХаосТом" , "итальнская")
newRestaurant1.describe_restaurant()

newRestaurant2 = Restaurant ("мамины чечевички" , "русская")
newRestaurant2.describe_restaurant()

newRestaurant3 = Restaurant ("Довольная рыба" , "паназиатская")
newRestaurant3.describe_restaurant()