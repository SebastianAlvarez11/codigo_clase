from abc import ABC, abstractclassmethod

class Animal():
    @abstractclassmethod
    def hacer_sonido(self)->str:
        pass