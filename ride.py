
import heapq


class Old_queue: 
    def __init__(self):
        self.heap = []

    def push(self,item):
        heapq.heappush(self.heap,(-item.year,item.inc,item))

    def preview(self,n):
        return [entry[2] for entry in heapq.nsmallest(n, self.heap)]

    def pop(self, n):
        return [heapq.heappop(self.heap)[2] for _ in range(min(n, len(self.heap)))]

    def list(self):
        return [entry[2] for entry in sorted(self.heap)]

    def __len__(self):
        return len(self.heap)


