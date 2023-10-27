class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner = {}):
        if pet_type in self.PET_TYPES:
            self.pet_type = pet_type
        else:
            raise Exception
        self.name = name
        self.owner = owner
        type(self).all.append(self)

class Owner:
    all = []

    def __init__(self, name):
        self.name = name
        type(self).all.append(self)
    
    def pets(self):
        return [pet for pet in Pet.all if pet.owner is self]
    
    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
            self.all.append(pet)
        else:
            raise Exception

    def get_sorted_pets(self):
        return sorted([pet for pet in Pet.all if pet.owner is self], key=lambda pet: pet.name)