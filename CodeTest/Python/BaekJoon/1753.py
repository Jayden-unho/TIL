import sys
import heapq
sys.stdin = open('input.txt')


def dijkstra():
    heap = [(0, K)]

    while heap:
        node = heapq.heappop(heap)
        if not visited[node[1]]:
            visited[node[1]] = 1
            distance[node[1]] = node[0]
            for e in linked[node[1]]:
                if not visited[e[1]]:
                    heapq.heappush(heap, (distance[node[1]]+e[0], e[1]))


V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())

linked = [[] for _ in range(V+1)]
visited = [0] * (V+1)
distance = [0] + [1e10]*(V)
distance[K] = 0

for _ in range(E):
    start, end, weight = map(int, sys.stdin.readline().split())
    linked[start].append((weight, end))
    # linked[start] = linked.get(start, []) + [(weight, end)]

dijkstra()

for i in range(1, len(distance)):
    if distance[i] == 1e10:
        print('INF')
    else:
        print(distance[i])