from src.animal import Animal

class Perro(Animal):
    def hacer_sonido(self)->str:
        print("Soy un perro.")