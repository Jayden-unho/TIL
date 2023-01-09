import sys
from collections import deque
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())
linked = [[] for _ in range(N)]
visited = [-1] * N

for _ in range(M):
    A, B = map(lambda x: int(x)-1, sys.stdin.readline().split())
    linked[A].append(B)
    linked[B].append(A)

q = deque([0])
visited[0] = 0

while q:
    node = q.popleft()
    for next_node in linked[node]:
        if visited[next_node] == -1:
            visited[next_node] = visited[node] + 1
            q.append(next_node)

ans_dist = max(visited)
ans_node = visited.index(ans_dist) + 1
ans_cnt = visited.count(ans_dist)

print(ans_node, ans_dist, ans_cnt)
