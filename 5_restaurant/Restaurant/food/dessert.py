from food.food import Food
class Dessert(Food):
    def __init__(self, name: str, price: float, gram: float,calories:float) -> None:
        super().__init__(name, price, gram)
        self.calories = calories
    def get_calories(self):
        return self.calories
