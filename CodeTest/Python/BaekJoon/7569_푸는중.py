'''
3차원 배열 -> 2차원 배열로 만들어서 진행
최소 기간이 필요하므로 DFS탐색
'''

import sys
from collections import deque


def delta_search():
    df = [0, 0, 0, 0, -1, 1]        # 위 / 오른쪽 / 아래 / 왼쪽 / 아랫층 / 윗층
    di = [-N, 1, N, -1, 0, 0]

    for f in range(H):              # Box floor
        for i in range(N):          # Box row & column
            for k in range(6):
                y = f + df[k]
                x = i + di[k]

                if 0 <= y < H and 0 <= x < M*N and box[y][x] == 0:
                    linked[(f, i)] = linked.get((f, i), []) + [y, x]                    


def dfs():
    q = deque(start)

    while q:
        node = q.popleft()
        visited[node[0]][node[1]] += 1
        print(node)
        for e in linked[node]:
            if not visited[e[0]][e[1]]:
                q.append(e)
                visited[e[0]][e[1]] = visited[node[0]][node[1]]


M, N, H = map(int, sys.stdin.readline().split())
box = []
linked = {}
visited = [[0]*(N*M) for _ in range(H+1)]

for i in range(H):                                              # 3차원 정보가 담긴 2차원 배열
    box.append([])
    for _ in range(N):
        box[i].extend(list(map(int, sys.stdin.readline().split())))

start = []
for a in range(H):
    for b in range(M*N):
        if box[a][b] == 1:
            start.append((a, b))

delta_search()
dfs()