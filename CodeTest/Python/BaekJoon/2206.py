import sys
from collections import deque
sys.stdin = open('input.txt')


def solution():
    # 초기 시작 세팅
    q = deque([(1, 0, 0)])
    visited[1][0][0] = 1

    while q:
        remain, y, x = q.popleft()
        visit = visited[remain][y][x]

        # 상하좌우 이동
        for k in range(4):
            ny = y + dr[k]
            nx = x + dc[k]

            if 0 <= ny < N and 0 <= nx < M:
                # 다음 좌표가 벽이 아닌 경우
                if not board[ny][nx] and visited[remain][ny][nx] > visit + 1:
                    visited[remain][ny][nx] = visit + 1
                    q.append((remain, ny, nx))
                # 다음 좌표가 벽인 경우
                elif board[ny][nx] == 1 and remain and visited[remain-1][ny][nx] > visit + 1:
                    visited[remain-1][ny][nx] = visit + 1
                    q.append((remain-1, ny, nx))


# 위, 오른쪽, 아래, 왼쪽
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 입력 정보, 행과 열, 맵 정보
N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(N)]

# 맵 좌표별 이동 위한 최소 거리
# 2개의 2차원 배열, 0번 인덱스의 2차원 배열: 벽을 한번 부수고 이동 시
# 1번 인덱스의 2차원 배열: 벽을 부수지 않고 이동 시
visited = [[[1e10] * M for _ in range(N)] for _ in range(2)]

solution()

# 벽 부순 경우, 부수지 않은 경우 중 최소 거리
answer = min(visited[0][N-1][M-1], visited[1][N-1][M-1])

# 이동 불가시 -1 출력, 최소 거리 출력
if answer == 1e10:
    print(-1)
else:
    print(answer)
