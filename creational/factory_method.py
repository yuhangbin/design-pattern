from abc import ABC, abstractmethod

# create a transport interface with a method to deliver

class Transport(ABC):
    @abstractmethod
    def deliver(self):
        pass

# implement the transport interface for a Truck and Ship

class Truck(Transport):
    def deliver(self):
        return "Delivering by truck"

class Ship(Transport):
    def deliver(self):
        return "Delivering by ship"
# create a logistic interface with a method to create a transport

class Logistic(ABC):
    @abstractmethod
    def create_transport(self):
        pass

# implement the logistic interface for a RoadLogistic and SeaLogistic

class RoadLogistic(Logistic):
    def create_transport(self):
        return Truck()

class SeaLogistic(Logistic):
    def create_transport(self):
        return Ship()


# main function and run the program

def main():
    road_logistic = RoadLogistic()
    sea_logistic = SeaLogistic()
    print(road_logistic.create_transport().deliver())
    print(sea_logistic.create_transport().deliver())

if __name__ == "__main__":
    main()

