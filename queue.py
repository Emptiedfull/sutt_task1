from collections import deque
from itertools import islice

class ride_queue:
    def __init__(self):
        self.items = deque()

    def push(self,item):
        self.items.append(item)

    def preview(self,n):
         return list(islice(self._items, k))

    def pop(self,n):
         return [self._items.popleft() for _ in range(min(n, len(self._items)))]

    def list(self):
        return list(self.items)

    def __len__(self):
        return len(list(self.items))


