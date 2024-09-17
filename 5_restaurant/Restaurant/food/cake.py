from food.dessert import Dessert
class Cake(Dessert):
    def __init__(self, name: str, price: float, gram: float, calories: float) -> None:
        super().__init__(name, price, gram, calories)
        self.gram = 250
        self.calories = 1000
        self.price = 5