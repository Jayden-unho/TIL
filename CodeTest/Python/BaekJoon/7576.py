'''
토마토가 모두 익는데 걸리는 최소 일자를 구해야하므로 BFS 이용
모든 토마토가 익어있으면 0
토마토가 모두 익지 못하면 -1 을 출력해야함
'''

import sys
from collections import deque



def bfs(start):
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    q = deque()
    q.extend(start)

    while q:
        node = q.popleft()
        visited[node[0]][node[1]] += 1

        for k in range(4):
            y = node[0] + dr[k]
            x = node[1] + dc[k]

            if 0 <= y < N and 0 <= x < M and box[y][x] == 0 and not visited[y][x]:
                visited[y][x] = visited[node[0]][node[1]]
                q.append((y, x))



M, N = map(int, sys.stdin.readline().split())
box = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

visited = [[0]*M for _ in range(N)]
start = []



for i in range(N):                  # 익은 토마토의 위치를 구함
    for j in range(M):
        if box[i][j] == 1:
            start.append((i, j))
        elif box[i][j] == -1:
            visited[i][j] = 1


bfs(start)


answer = 0
for i in range(N):
    if visited[i].count(0):
        answer = 0
        break

    elif answer < max(visited[i]):
        answer = max(visited[i])

print(answer - 1)