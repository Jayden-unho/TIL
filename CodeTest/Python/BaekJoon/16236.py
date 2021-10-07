import sys
from collections import deque
from pprint import pprint
sys.stdin = open('input.txt')


def bfs(start):
    q = deque()

    visited = [[0] * N for _ in range(N)]       # 물고기 먹으러 가는 길 체크 (한번 먹을때마다 길을 되돌아갈수있으므로 초기화)
    visited[start[0]][start[1]] = 1

    while q:
        node = q.popleft()
        for k in range(4):
            r = start[0] + dr[k]
            c = start[1] + dc[k]

            if 0 <= r < N and 0 <= c < N and shark_size >= sea[r][c] and not visited[r][c]:
                visited[r][c] = visited[node[0]][node[1]] + 1



dr = [-1, 0, 1, 0]      # 가장 위에 있는
dc = [0, -1, 0, 1]      # 가장 왼쪽에 있는

N = int(sys.stdin.readline())
sea = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
fish_info = {}          # 물고기들 정보 - 키: 크기 / 값 : 위치 좌표
shark_size = 2          # 상어 사이즈
time = 0

for i in range(N):
    for j in range(N):
        if sea[i][j]:
            fish_info[sea[i][j]] = fish_info.get(sea[i][j], []) + [(i, j)]

# print('----- fish_info -----')
# pprint(fish_info)

while shark_size > min(fish_info.keys()):
    pass

print(time)