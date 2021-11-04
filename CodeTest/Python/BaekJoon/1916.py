import sys
import heapq
sys.stdin = open('input.txt')


def dijkstra():
    heap = [(0, start)]

    while not visited[end]:
        node = heapq.heappop(heap)
        if not visited[node[1]]:
            visited[node[1]] = 1
            distance[node[1]] = node[0]
            for e in bus[node[1]]:
                if not visited[e[1]]:
                    heapq.heappush(heap, (distance[node[1]]+e[0], e[1]))


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

bus = [[] for _ in range(N+1)]
distance = [0] + [1e10]*N
visited = [0] * (N+1)

for _ in range(M):
    start, end, pay = map(int, sys.stdin.readline().split())
    bus[start].append((pay, end))

start, end = map(int, sys.stdin.readline().split())

dijkstra()

print(distance[end])