from collections import deque

class FIFO:
    def __init__(self, k, m, ids):
        self.k = k
        self.m = m
        self.ids = ids
        self.q = deque()
        self.cache = set()
        self.miss = 0

    def fifo(self):

        for id in self.ids:
            if id in self.cache:
                continue
            self.miss += 1

            if len(self.cache) == self.k:
                first = self.q.popleft()
                self.q.append(id)
                self.cache.remove(first)
                self.cache.add(id)
            else:
                self.q.append(id)
                self.cache.add(id)
        
        print(f"FIFO : {self.miss}")

    def printInfo(self):
        print(f"This is the queue: {self.q}")
        print(f"This is the cache: {self.cache}")
        print(f"This is the miss amount: {self.miss}")


#fifo(k,m,ids)