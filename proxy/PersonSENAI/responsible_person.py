from person import Person


class ResponsiblePerson:
    def __init__(self, person: Person):
        self.person = person

    def drink(self):
        if self.person.age >= 18:
            return self.person.drink()
        else:
            return 'muito jovem'

    def drive(self):
        if self.person.age >= 16:
            return self.person.drive()
        else:
            return 'muito jovem'

    def drink_and_drive(self):
        return 'morto'