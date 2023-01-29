import sys
import heapq
sys.stdin = open("input.txt")


def sol():
    global answer

    h = [(0, 0)]

    while h:
        weight, node = heapq.heappop(h)
        if visited[node]:
            continue

        visited[node] = 1
        answer -= weight
        for next_weight, next_node in linked[node]:
            if not visited[next_node]:
                heapq.heappush(h, (next_weight, next_node))


N, M = map(int, sys.stdin.readline().split())
linked = [[] for _ in range(N)]
visited = [0] * N
answer = 0

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    linked[a-1].append((c, b-1))
    linked[b-1].append((c, a-1))
    answer += c

sol()

if sum(visited) == N:
    print(answer)
else:
    print(-1)
