'''
8. Write a python program to create a CAR abstract class that contains an instance variable, a 
concrete method and two abstract methods. Also derive Maruti sub class from the CAR 
class and show implementation of abstract methods of CAR in subclass.
'''

from abc import ABC, abstractmethod

# Define abstract base class Car
class Car(ABC):
    def __init__(self, model):
        self.model = model

    # Concrete method
    def show_model(self):
        print(f"Car Model: {self.model}")

    # Abstract methods to be implemented by subclasses
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

# Define subclass Maruti that inherits from Car
class Maruti(Car):
    def __init__(self, model):
        super().__init__(model)

    # Implementation of abstract method start
    def start(self):
        print(f"{self.model} car started.")

    # Implementation of abstract method stop
    def stop(self):
        print(f"{self.model} car stopped.")


maruti_car = Maruti("Swift")

maruti_car.show_model()

maruti_car.start()
maruti_car.stop()

'''
Car Model: Swift
Swift car started.
Swift car stopped.
'''