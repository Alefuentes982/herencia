class Animal:
    def __init__(self, especie):
        self.especie = especie
    def describeme(self):
        print("Soy un Animal del tipo", type(self).__name__)


class Perro(Animal):
    pass

mi_perro = Perro('mamífero')
mi_perro.describeme()
