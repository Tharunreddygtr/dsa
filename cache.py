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


# LRU cache O(1) time complexity
class Node:
    def __init__(self, key, value):
        self.key =  key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def add(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

        

    def get(self, key: int) -> int:
        value = self.cache.get(key)
        if value:
            node = self.cache[key]
            self.remove(node)
            self.add(node)
            return node.value
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(key, value)
        self.add(node)
        self.cache[key] = node
        if len(self.cache.keys()) > self.capacity:
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
