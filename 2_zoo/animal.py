class Animal:
    def __init__(self, name:str):
        self.__name = name
    def getter(self):
        return self.__name