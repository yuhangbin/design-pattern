
from abc import ABC, abstractmethod


class Builder(ABC):
    @abstractmethod
    def set_seat(self, number_of_seats: int):
        pass

    @abstractmethod
    def set_engine(self, engine: str):
        pass
    def setGPS(self, has_gps: bool):
        pass
    def setTripComputer(self, has_trip_computer: bool):
        pass

class CarBuilder(Builder):
    def __init__(self):
        self.car = Car()

    def set_seat(self, number_of_seats: int):
        self.car.number_of_seats = number_of_seats
        return self

    def set_engine(self, engine: str):
        self.car.engine = engine
        return self

    def setGPS(self, has_gps: bool):
        self.car.has_gps = has_gps
        return self

    def setTripComputer(self, has_trip_computer: bool):
        self.car.has_trip_computer = has_trip_computer
        return self

    def get_result(self):
        return self.car
    
class Car:
    def __init__(self):
        self.number_of_seats = 0
        self.engine = ""
        self.has_gps = False
        self.has_trip_computer = False

    def __str__(self):
        return f"Car(number_of_seats={self.number_of_seats}, engine={self.engine}, has_gps={self.has_gps}, has_trip_computer={self.has_trip_computer})"

def main():
    builder = CarBuilder()
    car = builder.set_seat(4).set_engine("V8").setGPS(True).setTripComputer(True).get_result()
    print(car)

if __name__ == "__main__":
    main()  