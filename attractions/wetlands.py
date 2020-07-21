from .attraction import Attraction

class Wetlands(Attraction):

    def __init__(self, name, description):
        super().__init__(name, description)

        
    def add_animal(self, animal):
        try:
            if animal.swimming_speed > -1:
                self.animals.append(animal)
        except AttributeError:
            print(f'{animal} doesn\'t swim, it will die if you put it in {self.name} attraction.')