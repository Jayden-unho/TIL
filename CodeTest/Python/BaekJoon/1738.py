import sys
from collections import deque
sys.stdin = open('input.txt')


def bellmanford():
    for n in range(N):
        for i in range(N):
            for weight, node in linked[i]:
                if distance[i] != -1e10 and distance[node] < weight + distance[i]:
                    distance[node] = distance[i] + weight
                    paths[node] = i

                    if n == N-1:
                        distance[node] = 1e10


N, M = map(int, sys.stdin.readline().split())
linked = [[] for _ in range(N)]
distance = [-1e10] * N
distance[0] = 0
paths = [-1] * N

for _ in range(M):
    u, v, w = map(int, sys.stdin.readline().split())
    linked[u-1].append((w, v-1))

bellmanford()

if distance[-1] == 1e10:
    print(-1)
else:
    answer = deque([])
    node = N - 1

    while node >= 0:
        answer.appendleft(node+1)
        node = paths[node]

    print(*answer)
