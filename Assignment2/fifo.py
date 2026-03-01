

'''

Input:
- A cache of capacity ( k )
- A sequence of ( m ) requests ( r_1, r_2,.., r_m )




FIFO: Evict the item that has been in the cache the longest.


k m
r1 r2 r3 ... rm
Where:

( k ) = cache capacity ( ( k >= 1 ) )

( m ) = number of requests

( r_1, .., r_m ) = sequence of integer IDs


'''
from collections import deque
k = 3
m = 5
ids = [1,2,3,4,5,5]



def fifo(k,m,ids):
    q = deque()
    cache = set()
    miss = 0
    for id in ids:
        if id in cache:
            continue
        miss += 1

        if len(cache) == k:
            first = q.popleft()
            q.append(id)
            cache.remove(first)
            cache.add(id)
        else:
            q.append(id)
            cache.add(id)
    print(f"This is the queue: {q}")
    print(f"This is the cache: {cache}")
    print(f"This is the miss amount: {miss}")


fifo(k,m,ids)