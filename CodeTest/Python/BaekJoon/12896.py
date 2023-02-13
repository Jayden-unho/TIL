import sys
from collections import deque
sys.stdin = open('input.txt')


def BFS(start):
    q = deque([start])
    distance = [-1] * N
    distance[start] = 0

    while q:
        node = q.popleft()
        for next_node in linked[node]:
            if distance[next_node] == -1:
                distance[next_node] = distance[node] + 1
                q.append(next_node)

    return distance[node], node


N = int(sys.stdin.readline())
linked = [[] for _ in range(N)]
answer = 1e6

for _ in range(N-1):
    u, v = map(lambda x: int(x)-1, sys.stdin.readline().split())
    linked[u].append(v)
    linked[v].append(u)

idx = 0
for _ in range(2):
    dist, idx = BFS(idx)

if dist % 2:
    print(dist//2 + 1)
else:
    print(dist//2)
