'''
단방향 DFS
'''
import sys



def dfs(start):
    stack = [start]
    
    while stack:
        node = stack.pop()
        for e in linked[node]:
            if not visited[e-1]:
                visited[e-1] = 1
                stack.append(e)



N = int(sys.stdin.readline())
in_link = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
linked = [[] for _ in range(N+1)]

for i in range(N):
    for j in range(N):
        if in_link[i][j] == 1:
            linked[i+1].append(j+1)

for i in range(1, N+1):
    visited = [0] * N
    dfs(i)
    print(*visited)