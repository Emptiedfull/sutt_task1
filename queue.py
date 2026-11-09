from collections import deque
from itertools import islice

class Ride_queue:
    def __init__(self):
        self.items = deque()

    def push(self,item):
        self.items.append(item)

    def preview(self,n):
         return list(islice(self.items, n))

    def pop(self,n):
         return [self._items.popleft() for _ in range(min(n, len(self.items)))]

    def list(self):
        return list(self.items)

    def __len__(self):
        return len(list(self.items))


