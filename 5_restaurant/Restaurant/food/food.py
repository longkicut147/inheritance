import sys, os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append("C:/Users/Admin/Desktop/oop/inheritance/5_restaurant/")

from Restaurant.product import Product

class Food:
    def __init__(self,name:str,price:float,gram:float) -> None:
        self.name = name 
        self.price = price 
        self.gram = gram