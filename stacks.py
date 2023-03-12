class Stack:
    def __init__(self):
        self.data = []

    def push(self, item):
        return self.data.append(item)

    def pop(self):
        if len(self.data) == 0:
            return 'stack is empty'
        else:
            return self.data.pop()

    def size(self):
        return len(self.data)

    def top(self):
        return self.data[-1]

    def revstack(self):
        return self.data[::-1]


a = Stack()
a.push(5)
a.push(3)
a.push(7)
print(a.revstack())
