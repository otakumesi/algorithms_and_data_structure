class RingBuffer:
    def __init__(self, data_num = 10, initial_data = None):
        self.data_num = data_num
        self.index = 0

        if initial_data != None:
            self.data = initial_data
        else:
            self.data = [0] * data_num
        
    def insert(self, value):
        self.data[self.index] = value
        self.next()

    def next(self):
        self.index = self.next_index()

    def next_index(self):
        return (self.index + 1) % self.data_num

    def current_data(self):
        return self.data[self.index]

rb = RingBuffer(data_num=5, initial_data=[1, 2, 3, 4, 5])
import pdb; pdb.set_trace()
