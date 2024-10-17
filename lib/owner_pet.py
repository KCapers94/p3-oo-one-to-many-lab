class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    all = []
    
    def __init__(self, name, pet_type, owner= "None"):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        self.pet_type_check(pet_type)
        Pet.all.append(self)

    @classmethod
    def pet_type_check(cls, pet_type):
        if pet_type not in cls.PET_TYPES:
            raise Exception(f'{pet_type} not excepted')
        

class Owner:

    def __init__(self, name):
        self.name = name
        
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self 
        else:
            raise Exception ("Not a pet")
        
    def get_sorted_pets(self):
        pets_list = self.pets() 
        return sorted(pets_list, key=lambda pet: pet.name) 