from src.animal import Animal
from src.cuadrupedo import Cuadrupedo
from src.perro import Perro
from src.perro_salchicha import PerroSalchicha
from src.veterinario import Veterinario
from src.veterinario_especializado import VeterinarioEspecializado
from src.veterinario_para_perro import VeterinarioParaPerro

if __name__ == '__main__':
    animal = Animal()
    print(animal.hacer_sonido())
    perro = Perro()
    print(perro.hacer_sonido())
    cuadrupedo = Cuadrupedo()
    print(cuadrupedo.hacer_sonido())
    veterinario = Veterinario()
    print(veterinario.tratar_animal(Perro))
    veterinario2 = VeterinarioEspecializado()
    print(veterinario2.tratar_animal(Cuadrupedo))