class vehicle:
    def __init__(self):
        self.milage = None
        self.depth = None
        self.number = None
        self.Manufacturer = None
        self.capacity = None
        self.name = None
        self.width = None


class bus(vehicle):
    wheels = 6


class car(vehicle):
    wheels = 4


obj = vehicle()
obj_bus = bus()
a = 100


def testcase(a):
    assert a == 100
    return "Pass"


# print(obj_bus.wheels)
obj_car = car()


# print(obj_car.wheels)
# obj.milage=100
# print(obj.milage)
# print(testcase(a))
# string=input()
def binaryToDecimal(string):
    output = 0
    j = 0
    string = string[::-1]
    for i in range(len(string)):
        output += (2 ** j) * int(string[i])
        j += 1
    return output


# print(binaryToDecimal(string))

# integer=int(input())
def decimalToBinary(integer):
    list1 = []
    while integer > 0:
        list1.append(str(integer % 2))
        integer = integer // 2
    return "".join(list1[::-1])


def triangularPattern(size):
    for i in range(size):
        k = 0
        for j in range(size):
            print("*", end=" ")
        print()


size = 5


# triangularPattern(size)

def rightangled_triangularPattern(size):
    for i in range(size):
        k = 0
        for j in range(size):
            print("*", end=" ")
        print()


size = 5
# print(decimalToBinary(integer))
