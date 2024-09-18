class Product:
    def __init__(self,name:int,price:float) -> None:
        self.__name = name
        self.__price = price
        self.name = self.name()
        self.price = self.price()

    def name(self):
        return self.__name
    
    def price(self):
        return self.__price
    
