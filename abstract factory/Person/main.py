from person_factory import PersonFactory
     
  

person_factory = PersonFactory()

person_1 = person_factory.create_person('samara',32)
print(person_1.id, person_1.name)

person_2 = person_factory.create_person('ze', 45)
print(person_2.id, person_2.name)

person_3 = person_factory.create_person('ana',13)
print(person_3.id, person_3.name)

person_4 = person_factory.create_person('jose', 20)
print(person_4.id, person_4.name)


#self.listOfPeople, self.person_id, person_1, person_2, person_3 e person_4 são variáveis de referencia e armazenam os objetos criados pela factory