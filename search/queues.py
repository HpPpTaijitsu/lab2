import heapq
from collections import deque

class PriorityQueue:
    def __init__(self, items=(), key=lambda x: x):
        self.key = key
        self.items = []  # heap of (score, item) pairs
        for item in items:
            self.add(item)
    
    def add(self, item):
        pair = (self.key(item), item)
        heapq.heappush(self.items, pair)
    
    def pop(self):
        return heapq.heappop(self.items)[1]
    
    def top(self):
        return self.items[0][1]
    
    def __len__(self):
        return len(self.items)


class FIFOQueue:
    def __init__(self, items=()):
        self.items = deque(items)
    
    def pop(self):
        return self.items.popleft()
    
    def append(self, item):
        self.items.append(item)
    
    def appendleft(self, item):
        self.items.appendleft(item)
    
    def __len__(self):
        return len(self.items)