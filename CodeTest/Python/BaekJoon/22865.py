import sys
import heapq
sys.stdin = open('input.txt')


def dijkstra():
    h = [(0, A), (0, B), (0, C)]

    while h:
        dist, node = heapq.heappop(h)
        if distance[node] > dist:
            distance[node] = dist
            for next in linked[node]:
                # heap 시간복잡도 단축
                if distance[next[1]] > dist + next[0]:
                    heapq.heappush(h, (dist + next[0], next[1]))


N = int(sys.stdin.readline())
A, B, C = map(lambda x: int(x) - 1, sys.stdin.readline().split())
linked = [[] for _ in range(N)]
distance = [1e10] * N

for _ in range(int(sys.stdin.readline())):
    D, E, L = map(int, sys.stdin.readline().split())
    linked[D-1].append((L, E-1))
    linked[E-1].append((L, D-1))

dijkstra()

answer = distance.index(max(distance)) + 1

print(answer)
