# Base class representing a general book
class Book:
    def __init__(self, title, author, genre, pages):
        """
        Initialize a Book object.
        """
        self.title = title
        self.author = author
        self.__genre = genre # Private attribute 
        self.pages = pages


# 2
# Base class
class Vehicle:
    def move(self):
        """
        Define a generic move method for vehicles.
        """
        print("This vehicle moves in some way.")

# Car class
class Car(Vehicle):
    def move(self):
        """
        Override the move method for Car.
        """
        print("Driving 🚗")

# Plane class
class Plane(Vehicle):
    def move(self):
        """
        Override the move method for Plane.
        """
        print("Flying ✈️")

# Boat class
class Boat(Vehicle):
    def move(self):
        """
        Override the move method for Boat.
        """
        print("Sailing 🚤")

# Train class
class Train(Vehicle):
    def move(self):
        """
        Override the move method for Train.
        """
        print("Riding on rails 🚆")

# Function to demonstrate polymorphism
def demonstrate_movement(vehicles):
    """
    Demonstrates how different vehicles move using polymorphism.
    """
    for vehicle in vehicles:
        vehicle.move()

# Example usage
if __name__ == "__main__":
    # Create instances of different vehicles
    car = Car()
    plane = Plane()
    boat = Boat()
    train = Train()

    # Store vehicles in a list
    vehicles = [car, plane, boat, train]

    # Demonstrate polymorphism
    demonstrate_movement(vehicles)


