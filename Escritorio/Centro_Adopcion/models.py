class Dog:
    def __init__(self, dog_id, name, age, breed, adopted=False):
        self.id = dog_id
        self.name = name
        self.age = age
        self.breed = breed
        self.adopted = adopted


class Adopter:
    def __init__(self, adopter_id, name, lastName, address, id_card=None):
        self.adopter_id = adopter_id  # Referencia a Person.id
        self.name = name
        self.lastName = lastName
        self.address = address
        self.id_card = id_card


class Adoption:
    def __init__(self, id, dog_id, adopter_id, adoption_date):
        self.id = id
        self.dog_id = dog_id
        self.adopter_id = adopter_id
        self.adoption_date = adoption_date