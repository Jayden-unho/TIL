"""
최소 스패닝 문제 (Minimum Spanning Tree)

1. prim - default
1-1. prim - heapq
2. kruskal
"""

import sys
import heapq
sys.stdin = open('input.txt')

"""
# 1. prim - default
# 실행시간이 느림, 메모리 많이 사용
def prim():
    for _ in range(V):
        min_idx = -1
        min_distance = 1e10

        for i in range(1, V+1):
            if not visited[i] and distance[i] < min_distance:
                min_idx = i
                min_distance = distance[i]
        visited[min_idx] = 1

        for e in linked.get(min_idx, []):
            if not visited[e[1]] and distance[e[1]] > e[0]:
                distance[e[1]] = e[0]


# 1-1. prim - heapq
# 실행시간 조금 느림 (python -> Memory 68 mb, Time - 912 ms)
def heap_prim():
    heap = [(0, 1)]

    while heap:
        node = heapq.heappop(heap)
        if not visited[node[1]]:
            distance[node[1]] = node[0]
            visited[node[1]] = 1
            for e in linked[node[1]]:
                heapq.heappush(heap, (e[0], e[1]))


V, E = map(int, sys.stdin.readline().split())

linked = {}
kruskal_link = []
distance = [0] + ([1e10] * V)
distance[1] = 0
visited = [0] * (V+1)

for _ in range(E):
    start, end, weight = map(int, sys.stdin.readline().split())
    linked[start] = linked.get(start, []) + [(weight, end)]
    linked[end] = linked.get(end, []) + [(weight, start)]

prim()
heap_prim()
"""

# 2. kruskal
# 실행시간 빠름 (python -> Memory - 54 mb / Time - 400 ms)
def find_set(x):
    if x != s[x]:
        s[x] = find_set(s[x])
    return s[x]


def union(x, y):
    s[find_set(y)] = find_set(x)


def kruskal():
    global answer 

    edge_cnt, idx = 0, 0

    while edge_cnt != V-1:
        x = linked[idx][0]
        y = linked[idx][1]

        while find_set(x) != find_set(y):
            union(x, y)
            edge_cnt += 1
            answer += linked[idx][2]
        idx += 1


V, E = map(int, sys.stdin.readline().split())

s = [x for x in range(V+1)]
linked = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(E)], key=lambda x: x[2])
answer = 0

kruskal()
print(answer)