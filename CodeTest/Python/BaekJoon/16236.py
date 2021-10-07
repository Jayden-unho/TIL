import sys
from collections import deque
from pprint import pprint
sys.stdin = open('input.txt')


def bfs(i, j):
    global time, eat_cnt, shark_size, shark_coordinate

    q = deque()
    q.append((i, j))
    visited = [[0] * N for _ in range(N)]
    visited[i][j] = 1

    while q:
        node = q.popleft()
        
        for k in range(4):
            r = node[0] + dr[k]
            c = node[1] + dc[k]

            if 0 <= r < N and 0 <= c < N and not visited[r][c] and sea[r][c] <= shark_size:
                visited[r][c] = visited[node[0]][node[1]] + 1
                if sea[r][c] and shark_size > sea[r][c]:
                    sea[r][c] = 0
                    sea[shark_coordinate[0]][shark_coordinate[1]] = 0
                    shark_coordinate = [r, c]
                    eat_cnt += 1
                    if eat_cnt == shark_size:
                        shark_size += 1
                        eat_cnt = 0
                    time += (visited[r][c] - 1)
                    return True

                q.append((r, c))
    return False


dr = [-1, 0, 1, 0]      # 가장 위에 있는
dc = [0, -1, 0, 1]      # 가장 왼쪽에 있는

N = int(sys.stdin.readline())
sea = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
fish_cnt = [0] * 7      # 사이즈별 남은 상어 수
shark_coordinate = []   # 상어 위치
eat_cnt = 0             # 상어가 먹은 횟수
shark_size = 2          # 상어 사이즈
time = 0                # 흐른 시간

for i in range(N):                          # 바다에서 물고기와 상어의 정보를 정리함
    for j in range(N):
        if sea[i][j] == 9:
            shark_coordinate = [i, j]
        elif sea[i][j]:
            fish_cnt[sea[i][j]] += 1

while True:       # 상어보다 작은 크기의 물고기가 있다면
    if not bfs(shark_coordinate[0], shark_coordinate[1]):
        break

print(sea)
print(time)