from food.main_dish import Main_dish
class Salmon(Main_dish):
    def __init__(self, name: str, price: float) -> None:
        super().__init__(name, price)
        self.gram = 22 