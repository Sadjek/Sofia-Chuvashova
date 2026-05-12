class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Название ресторана: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")

    def open_restaurant(self):
        print("Ресторан открыт!")

    stars = 1
    def change_stars(self, stars):
        self.stars = stars
        print(f'Звёзд у ресторана: {stars}')


newRestaurant1 = Restaurant ("мамины чечевички" , "русская")
newRestaurant1.describe_restaurant()
newRestaurant1.change_stars(5)