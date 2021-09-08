import sys
from collections import deque



def dfs(start):
    q = deque([start])
    visited[start] = 1

    while q:
        node = q.popleft()
        for idx in range(1, 7):
            if not visited[board[node+idx]]:
                visited[board[node+idx]] = visited[node] + 1
                q.append(board[node+idx])
            
            if visited[100]:
                return
                



N, M = map(int, input().split())
board = [x for x in range(101)]
visited = [0] * 101

for _ in range(N):
    x, y = map(int, input().split())
    board[x] = y

for _ in range(M):
    u, v = map(int, input().split())
    board[u] = v

dfs(1)
print(visited[100] - 1)