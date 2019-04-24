class PriorityQueue:
    def __init__(self):
        self.heap = []

    def enqueue(self, value):
        self.heap = self.heap + [value]

        i = len(self.heap) - 1

        while i > 0:
            parent_idx = (i-1) // 2
            if self.heap[parent_idx] > self.heap[i]:
                self._swap(parent_idx, i)
            i = parent_idx

    def dequeue(self):
        value = self.heap[0]

        last_index = len(self.heap) - 1
        self.heap[0] = self.heap[last_index]
        del self.heap[last_index]

        i = 0
        while i < (last_index-1) // 2:
            left_child_idx = i*2+1
            right_child_idx = i*2+2
            if self.heap[i] > left_child_idx:
                if self.heap[left_child_idx]> self.heap[right_child_idx]:
                    self._swap(right_child_idx, i)
                    i = right_child_idx
                else:
                    self._swap(left_child_idx, i)
                    i = left_child_idx
            elif(self.heap[i] > self.heap[right_child_idx]):
                self._swap(right_child_idx, i)
                i = right_child_idx
            else:
                return value

        return value

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __str__(self):
        return str(self.heap)

pq = PriorityQueue()
pq.enqueue(5)
pq.enqueue(2)
pq.enqueue(6)
pq.enqueue(4)
pq.enqueue(1)
import pdb;pdb.set_trace()
