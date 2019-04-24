class Stack:
    def __init__(self):
        self.storage = []

    def push(self, value):
        self.storage = self.storage + [value]

    def pop(self):
        last_index = len(self.storage)
        value = self.storage[last_index - 1]
        del self.storage[last_index - 1]
        return value

    def show(self):
        print(self)

    def __str__(self):
        return str(self.storage)

import pdb; pdb.set_trace()
