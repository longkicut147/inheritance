import sys, os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append("C:/Users/Admin/Desktop/oop/inheritance/5_restaurant/")

from Restaurant.product import Product

class Beverage(Product):
    def __init__(self, name: int, price: float,milliliters:float) -> None:
        super().__init__(name, price)
        self.milliliters = milliliters 
