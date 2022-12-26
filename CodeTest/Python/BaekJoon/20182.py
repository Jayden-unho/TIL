import sys
import heapq
sys.stdin = open('input.txt')


def sol():
    h = [(0, A, C)]

    while h:
        weight, node, remain = heapq.heappop(h)
        if weights[node] <= weight:
            continue

        weights[node] = weight
        for next_weight, next_node in linked[node]:
            max_weight = max(weight, next_weight)
            next_remain = remain - next_weight
            if next_remain >= 0 and weights[next_node] > max_weight:
                heapq.heappush(h, (max_weight, next_node, next_remain))


N, M, A, B, C = map(int, sys.stdin.readline().split())
linked = [[] for _ in range(N+1)]
weights = [1e10] * (N+1)

for _ in range(M):
    S, E, W = map(int, sys.stdin.readline().split())
    linked[S].append((W, E))
    linked[E].append((W, S))

sol()

print(-1 if weights[B] == 1e10 else weights[B])
