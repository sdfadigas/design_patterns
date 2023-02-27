from builder import Builder
from car import Car


class Director:
    def _init_(self):
        self.__builder = None

    def set_builder(self, builder: Builder):
        self.__builder = builder

    def get_car(self) -> Car:
        car = Car()
        car.set_body(self.__builder.get_body())
        car.set_engine(self.__builder.get_engine())
        for i in range(4):
            car.attach_wheel(self.__builder.get_wheel())
        return car

director = Director()