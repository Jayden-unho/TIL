import sys
import heapq
from collections import deque
sys.stdin = open('input.txt')


# 특정 좌표에서 다른 로봇 또는 열쇠 좌표까지의 거리 구하기
def bfs(y, x):
    visited = [[0] * N for _ in range(N)]
    q = deque([(y, x)])
    visited[y][x] = 1

    while q:
        r, c = q.popleft()
        visit = visited[r][c]

        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]

            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and maze[nr][nc] != '1':
                # 다음 좌표가 다른 로봇 또는 열쇠 좌표인 경우, 딕셔너리에 추가
                if maze[nr][nc] in {'K', 'S'}:
                    nodes[(nr, nc)] = nodes.get(
                        (nr, nc), []) + [(visit, (y, x))]
                visited[nr][nc] = visit + 1
                q.append((nr, nc))


# 로봇과 열쇠의 최단 거리를 연결하여 움직인 횟수의 최솟값 구하기
def solution(y, x):
    h = [(0, (y, x))]
    ans = 0
    visited = set()

    while h:
        weight, coor = heapq.heappop(h)
        if coor not in visited:
            visited.add(coor)
            ans += weight
            for next in nodes[coor]:
                heapq.heappush(h, next)

    return ans


# 위, 오른쪽, 아래, 왼쪽
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 입력 데이터
N, M = map(int, sys.stdin.readline().split())
maze = [list(sys.stdin.readline().strip()) for _ in range(N)]

# 로봇 또는 열쇠들의 각 좌표간 거리 정보
nodes = {}

for i in range(N):
    for j in range(N):
        # 로봇이거나 열쇠인 좌표일때만 BFS 탐색
        if maze[i][j] in {'S', 'K'}:
            bfs(i, j)

            # 모두 연결되어 있는게 아니라면, -1 출력 및 종료
            if len(nodes.keys()) < M:
                print(-1)
                exit(0)

# 최소 거리 구하기
print(solution(*list(nodes.keys())[0]))
