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


# LRU CACHE  USING DICT AND LISTS 

dict1 = {}
list1 = [['put', [10, "two"]],  ['put', [3, "three"]], ['put', [4, "four"]], ["get", 3]]
capacity = 2
for ele in list1:
    if ele[0] == "put":
        if len(dict1.keys()) >= capacity:
            del dict1[list(dict1.keys())[0]]
        key = ele[1][0]
        value = ele[1][1]
        dict1[key] = value
        print(dict1)
    else:
        key = ele[1]
        value = dict1[key]
        del dict1[key]
        dict1[key] = value
        print(dict1)
