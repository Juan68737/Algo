

from collections import defaultdict,deque, OrderedDict

class OPTFF:
    def __init__(self, k,m,ids):
        self.k = k
        self.m = m
        self.ids = ids
        self.cache = set()
        self.miss = 0
        self.seen = {}
        self.n = len(self.ids)
        self.future = [-1] * self.n
        self.futureMap = {}
        self.nextUse = {}

        for i in range(self.n - 1, -1, -1):
            self.future[i] = self.seen.get(self.ids[i], -1)
            self.seen[self.ids[i]] = i
        for i,num in enumerate(self.future):
            self.futureMap[i] = num

    def optff(self):

        for i, id in enumerate(self.ids):

            if id in self.cache:
                self.nextUse[id] = self.future[i] 
                #self.orderedList[id] = self.future[i] 
                #self.orderedList.move_to_end(id)
                continue

            '''
            if id in cache:
                
                orderedList[id] = futureMap[id]
                orderedList.move_to_end(id)
                continue
            '''
            self.miss += 1

            if len(self.cache) == self.k:
                check = []

                for id_in_cache in self.cache:
                    nextUse = self.nextUse.get(id_in_cache, -1)
                    if nextUse == -1:
                        nextUse = float("inf")
                    check.append((id_in_cache, nextUse))


                #check = [(id_in_cache, futureMap[id_in_cache]) for id_in_cache in cache]
                check.sort(key=lambda x: x[1])
                remove_id, _ = check[-1]
                self.cache.remove(remove_id)
                self.nextUse.pop(remove_id, None)
                #self.orderedList.pop(remove_id, None)
            self.cache.add(id)
            self.nextUse[id] = self.future[i]
            #self.orderedList[id] = self.future[i]
            #self.orderedList.move_to_end(id)
        print(F"OPTFF : {self.miss}")

    def printInfo(self):
        print(f"This is the cache: {self.cache}")
        print(f"This is the miss amount: {self.miss}")




