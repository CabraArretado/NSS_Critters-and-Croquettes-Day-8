from . import Animal
from movements import Walking

class Llama(Animal, Walking):

    def __init__(self, name, species, food, shift):
        Animal.__init__(self, name, species, food)
        Walking.__init__(self)
        self.shift = shift

    def __str__(self):
        return f'{self.name} the Llama'