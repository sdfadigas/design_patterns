from director import Director
from land_rover_builder import LandRoverBuilder
from porsche_builder import PorscheBuilder

director = Director()

print("\n------------------------------------\n")

land_rover_builder = LandRoverBuilder()
director.set_builder(land_rover_builder)
jeep = director.get_car()
jeep.specification()

print("\n------------------------------------\n")

porsche_builder = PorscheBuilder()
director.set_builder(porsche_builder)
porsche = director.get_car()
porsche.specification()
print("\n------------------------------------\n")
