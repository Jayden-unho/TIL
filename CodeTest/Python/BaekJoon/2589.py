import sys
from collections import deque
sys.stdin = open('input.txt')

dr = [-1, 0, 1, 0]      # 위 오른쪽 아래 왼쪽
dc = [0, 1, 0, -1]

def solution(y, x):
    q = deque([(y, x)])
    visited = [[-1] * C for _ in range(R)]      # 시작점에서 특정 지점까지 거리
    visited[y][x] = 0                           # 시작점은 거리 0으로 할당

    while q:
        node = q.popleft()          # 육지 좌표
        for k in range(4):
            r = node[0] + dr[k]     # 다음 탐색할 좌표
            c = node[1] + dc[k]

            if 0 <= r < R and 0 <= c < C and visited[r][c] == -1 and board[r][c] == 'L':
                # 다음 좌표가 범위 내이고 아직 방문하지 않았으며, 육지인 경우
                visited[r][c] = visited[node[0]][node[1]] + 1       # 해당 위치까지 거리 기록
                q.append((r, c))

    return visited[node[0]][node[1]]                                # 가장 먼 육지까지 거리 반환


R, C = map(int, sys.stdin.readline().split())                       # 세로, 가로
board = [list(sys.stdin.readline().rstrip()) for _ in range(R)]     # 입력 정보
answer = 0

for i in range(R):
    for j in range(C):
        if board[i][j] == 'L':              # 2차원 배열을 순환하며 육지인 경우에
            ans = solution(i, j)            # 현재 좌표에서 다른 육지로 가는 가장 긴 거리
            answer = max(ans, answer)       # 이전 거리와 현재 값 중 가장 긴 거리를 저장

print(answer)