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


# LRU CACHE  O(n) time complexity but need to be O(1)

class Cache:
    def __init__(self, size):
        self.size = size
        self.cache = {}
        self.head = None
        self.tail = None
    def put(self, key, value):
        if self.head is None:
            self.head = key
        if len(self.cache.keys()) >= self.size:
            del self.cache[list(self.cache.keys())[0]]
            # del self.cache[head]
        self.cache[key] = value
        
        print(self.cache)
        
    def get(self, key):
        value = self.cache.get(key)
        if value:
            del self.cache[key]
            self.cache[key] = value
        print(self.cache)


c = Cache(3)
# Cache of size 2

c.put("hello", 1) 

c.put("world", 2) 

c.put("demo", 3)
c.get("world")
c.put("demo1", 4)
c.put("demo2", 5)
