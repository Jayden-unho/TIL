import sys
from collections import deque
sys.stdin = open('input.txt')


def bfs(i, j):
    global m_time, shark_size, visited

    q = deque([(i, j)])
    visited = [[0] * N for _ in range(N)]
    visited[i][j] = 1
    end_num = 1e10

    while q:
        node = q.popleft()

        for k in range(4):
            r = node[0] + dr[k]
            c = node[1] + dc[k]

            if 0 <= r < N and 0 <= c < N and not visited[r][c] and sea[r][c] <= shark_size:
                visited[r][c] = visited[node[0]][node[1]] + 1
                if visited[r][c] > end_num:
                    return
                q.append((r, c))

                if sea[r][c] and shark_size > sea[r][c]:
                    can_eat.append([r, c])
                    end_num = visited[r][c]


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]      

N = int(sys.stdin.readline())
sea = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
shark_coordinate = []   # 상어 위치
eat_cnt = 0             # 상어가 먹은 횟수
shark_size = 2          # 상어 사이즈
m_time = 0              # 흐른 시간
can_eat = []            # 먹을수있는 물고기 리스트

for i in range(N):                          # 바다에서 물고기와 상어의 정보를 정리함
    for j in range(N):
        if sea[i][j] == 9:
            sea[i][j] = 0
            shark_coordinate = [i, j]
            break

while True:       # 상어보다 작은 크기의 물고기가 있다면
    bfs(shark_coordinate[0], shark_coordinate[1])

    if not can_eat:
        break

    tmp = sorted(can_eat, key=lambda x: (x[0], x[1]), reverse=True).pop()
    shark_coordinate = [tmp[0], tmp[1]]
    sea[tmp[0]][tmp[1]] = 0
    eat_cnt += 1
    if eat_cnt == shark_size:
        shark_size += 1
        eat_cnt = 0
    m_time += (visited[tmp[0]][tmp[1]] - 1)
    can_eat.clear()

print(m_time)