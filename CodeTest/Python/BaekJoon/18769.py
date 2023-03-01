import sys
import heapq
sys.stdin = open('input.txt')


def sol():
    h = [(0, 0)]
    distance = [False] * N
    result = 0

    while h:
        w, n = heapq.heappop(h)
        if not distance[n]:
            distance[n] = True
            result += w
            for next_w, next_n in linked[n]:
                if not distance[next_n]:
                    heapq.heappush(h, (next_w, next_n))

    return result


for _ in range(int(sys.stdin.readline())):
    R, C = map(int, sys.stdin.readline().split())
    N = R * C
    linked = [[] for _ in range(N)]

    # 수평
    for i in range(R):
        weights = list(map(int, sys.stdin.readline().split()))
        for j in range(C-1):
            w = weights[j]
            left, right = i*C+j, i*C+j+1
            linked[left].append((w, right))
            linked[right].append((w, left))

    # 수직
    for i in range(R-1):
        weights = list(map(int, sys.stdin.readline().split()))
        for j in range(C):
            w = weights[j]
            up, down = i*C+j, (i+1)*C+j
            linked[up].append((w, down))
            linked[down].append((w, up))

    print(sol())
