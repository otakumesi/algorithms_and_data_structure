class Queue:
    def __init__(self):
        self.storage = []

    def enqueue(self, value):
        self.storage = self.storage + [value]

    def dequeue(self):
        value = self.storage[0]
        del self.storage[0]
        return value

    def show(self):
        print(self)

    def __str__(self):
        return str(self.storage)

import pdb; pdb.set_trace()
