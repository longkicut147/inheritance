from food.food import Food
class Starter(Food):
    def __init__(self, name: str, price: float, gram: float) -> None:
        super().__init__(name, price, gram)