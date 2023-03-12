class Vehicle:
    def __init__(self):
        self.mileage = None
        self.depth = None
        self.number = None
        self.manufacturer = None
        self.capacity = None
        self.name = None
        self.width = None


class Bus(Vehicle):
    def __init__(self, wheels):
        self.wheels = wheels
        super().__init__()


obj = Vehicle
obj.mileage = 100
print(obj.mileage)
