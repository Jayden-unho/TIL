import sys
from collections import deque
sys.stdin = open('input.txt')


def sol(start):
    q = deque([(1e10, start)])
    distance[start][start] = 0

    while q:
        dist, node = q.popleft()
        for next_dist, next_node in linked[node]:
            if distance[start][next_node] == 1e10:
                num = min(next_dist, dist)
                distance[start][next_node] = num
                q.append((num, next_node))


N, Q = map(int, sys.stdin.readline().split())
linked = [[] for _ in range(N)]
distance = [[1e10] * N for _ in range(N)]

for _ in range(N-1):
    p, q, r = map(int, sys.stdin.readline().split())
    linked[p-1].append((r, q-1))
    linked[q-1].append((r, p-1))

for _ in range(Q):
    k, v = map(int, sys.stdin.readline().split())

    if distance[v-1][v-1] != 0:
        sol(v-1)

    print(len(list(filter(lambda x: x >= k, distance[v-1]))))
