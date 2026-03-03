from collections import OrderedDict

class LRU:
    def __init__(self, k, m, ids):
        self.k = k
        self.m = m
        self.ids = ids
        self.cache = OrderedDict()
        self.miss = 0

    def lru(self):
        for id in self.ids:
            if id in self.cache:
                self.cache.move_to_end(id)
            else:
                if len(self.cache) == self.k:
                    self.cache.popitem(last=False)
                self.cache[id] = True
                self.cache.move_to_end(id)
                self.miss += 1
        
        print(f"LRU : {self.miss}")

    def printInfo(self):
        print(f"This is the capcaity: {self.k}")
        print(f"This is the cache: {[id for id, _ in self.cache.items()]}")
        print(f"This is the miss amount: {self.miss}")

#lru(k,m,ids)



