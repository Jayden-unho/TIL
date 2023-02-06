import sys
import heapq
sys.stdin = open("input.txt")

N, M = map(int, sys.stdin.readline().split())
S, E = map(int, sys.stdin.readline().split())
linked = [[] for _ in range(N+1)]

for _ in range(M):
    h1, h2, k = map(int, sys.stdin.readline().split())
    linked[h1].append((-k, h2))
    linked[h2].append((-k, h1))

h = [(-1e6, S)]
visited = [0] * (N+1)

while h:
    weight, node = heapq.heappop(h)
    if not visited[node]:
        visited[node] = min(visited[node], weight)
        for next_weight, next_node in linked[node]:
            if not visited[next_node]:
                heapq.heappush(h, (max(next_weight, weight), next_node))

print(-visited[E])
