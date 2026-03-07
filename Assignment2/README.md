**Jhonathan Herrera (82264230) & Jason Guan (28702814)**

**Instructions to run the code:**

cd Assignment2
cd src
run:
python3 main.py ../input/<any .in file>

example:
python3 main.py ../input/example2.in

output:
FIFO : 5
LRU : 4
OPTFF : 4

**solutions to the written component**

1.

| Input File  | k   | m   | FIFO | LRU | OPTFF |
| ----------- | --- | --- | ---- | --- | ----- |
| q1_case1.in | 4   | 60  | 50   | 40  | 18    |
| q1_case2.in | 3   | 60  | 60   | 60  | 38    |
| q1_case3.in | 5   | 60  | 39   | 27  | 19    |

Yes, OPTFF has the fewest misses in all three files: 18 < 40 < 50 (File1), 38 < 60 = 60 (File2), and 19 < 27 < 39 (File3).

For FIFO vs LRU: LRU performs better on File1 and File3 (40 vs 50, and 27 vs 39), while FIFO and LRU tie on File2 (both 60).

2. Yes, there is a sequence that exists for (k=3). If we use the sequence: (1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5)

Miss counts: FIFO: 9 LRU: 10 OPTFF: 7

This shows OPTFF has fewer misses than both FIFO and LRU ((7 < 9) and (7 < 10)).

The reasoning is that OPTFF is offline and removes the item or element whose next usage is farthest in the future, so it preserves or protects the items or elements needed soon.

FIFO only uses First In, First Out, and LRU only uses Least Recently Used.

In this sequence and situation, those removals created extra misses for FIFO/LRU, while OPTFF avoids several of them.

3. Let the request sequence be r1, … , rm and cache size k.

We will define OPTFF as the following: on a miss with full cache, remove the cached page whose next request is the farthest in the future (or never requested again).

We can prove with the following:
Take A, the offline algorithm.

Compare OPTFF and A from the start, and let t be the first time they make different eviction or removal choices.

At time t, both see the same future and the same cache contents (up to this very first disagreement), and both must evict one item or element.

OPTFF evicts or removes page x, where the next usage of x is the farthest.
A evicts or removes some other page y.

Create a new algorithm A′ identical to A.

However, for this algorithm, the only time it is different is at time t where it evicts or removes x (same as OPTFF), and after that it behaves like A with the names of x, y swapped until one of them is requested.
Since the next usage of x ≥ the next usage of y, page y is needed no later than x.
Therefore, replacing y by x at time t cannot create an earlier extra miss. Before x is needed, A' is never worse than the A algorithm.
When one of {x, y} is requested, the swap with the interval ends, and from then on A' can be like A without increasing misses.
So A' has no more misses than A, and now agrees with OPTFF.
Therefore, misses(OPTFF) ≤ misses(A).
