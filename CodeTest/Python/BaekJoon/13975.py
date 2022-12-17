import sys
import heapq as h
sys.stdin = open('input.txt')

for _ in range(int(sys.stdin.readline())):
    K = int(sys.stdin.readline())
    answer = 0
    dict = {}

    for num in map(int, sys.stdin.readline().split()):
        dict[num] = dict.get(num, 0) + 1

    heap = list(dict.keys())
    h.heapify(heap)

    for _ in range(K-1):
        n = heap[0]

        if dict.get(n, 0) > 1:
            dict[n] -= 2
            if not dict[n]:
                h.heappop(heap)
            result = n * 2
        else:
            h.heappop(heap)
            m = heap[0]
            dict[n] -= 1
            dict[m] -= 1
            if not dict[m]:
                h.heappop(heap)
            result = n + m

        dict.get(result, False) or h.heappush(heap, result)
        dict[result] = dict.get(result, 0) + 1

        answer += result

    print(answer)
