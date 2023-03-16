from person import Person
class PersonFactory:
    def __init__(self):
        self.listOfPeople = []
        self.person_id = 0
    
    def create_person(self, name, age):
        new_person = Person(self.person_id, name, age)
        self.listOfPeople.append(new_person)
        self.person_id += 1
        return new_person      