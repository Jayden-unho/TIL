import sys
sys.stdin = open('input.txt')


def dfs(y, x):
    stack = [(y, x)]
    visited[y][x] = True
    cnt = 1

    while stack:
        r, c = stack.pop()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]

            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and images[nr][nc]:
                visited[nr][nc] = True
                stack.append((nr, nc))
                cnt += 1
    return cnt


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

N, M = map(int, sys.stdin.readline().split())
images = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
num = 0
count = 0

for i in range(N):
    for j in range(M):
        if images[i][j] and not visited[i][j]:
            num += 1
            count = max(dfs(i, j), count)

print(num)
print(count)
