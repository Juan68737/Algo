import sys
from lru import LRU
from fifo import FIFO
from optff import OPTFF





with open(sys.argv[1], "r") as f:
    k, m =  map(int, f.readline().split())

    r = [int(x) for x in f.readline().strip().split()] 


lru = LRU(k,m,r)
lru.lru()
fifo = FIFO(k,m,r)
fifo.fifo()
optff = OPTFF(k,m,r)
optff.optff()