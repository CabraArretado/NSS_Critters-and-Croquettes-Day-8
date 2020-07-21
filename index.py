from animals import Goose, Llama
from attractions import PettingZoo


miss_fuzz = Llama("Miss Fuzz", "domesticated llama", "oats", "morning")
bob = Goose("Bob", "Canada goose", "Goose Chow")

varmint_village = PettingZoo("The Varmint Village", "The cozy village")
varmint_village.add_animal_pythonic(bob)
varmint_village.add_animal_type_check(bob)
varmint_village.add_animal_pythonic(miss_fuzz)

for animal in varmint_village.animals:
    print(f'{animal} lives in Varmint Village.')