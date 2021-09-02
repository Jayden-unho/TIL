import sys
import heapq


N = int(sys.stdin.readline())
heap = []
signs = []

for _ in range(N):
    x = int(sys.stdin.readline())

    if not x:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (abs(x), x))