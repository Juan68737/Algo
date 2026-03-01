from collections import OrderedDict



k = 3
m = 5
ids = [1,2,3,4,5,5]
capacity = 3
cache = OrderedDict()

def lru(k,m,ids):
    capacity = k
    cache = OrderedDict()
    miss = 0
    for id in ids:
        if id in cache:
            cache.move_to_end(id)
        else:
            if len(cache) == capacity:
                cache.popitem(last=False)
            cache[id] = True
            cache.move_to_end(id)
            miss += 1
    print(f"This is the capcaity: {capacity}")
    print(f"This is the cache: {[id for id, _ in cache.items()]}")
    print(f"This is the miss amount: {miss}")

lru(k,m,ids)



