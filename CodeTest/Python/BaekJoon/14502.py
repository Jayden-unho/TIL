import sys
from collections import deque
from itertools import combinations
sys.stdin = open('input.txt')

def solution():
    global ans

    q = deque(start_coordinates)                # 바이러스가 있는 모든곳에서 시작 (BFS)

    while q:
        node = q.popleft()
        for k in range(4):
            r = node[0] + dr[k]
            c = node[1] + dc[k]

            # 바이러스가 감염이 가능한 구역이면, 방문처리, 안전구역 1 감소, 다음 탐색 위한 추가
            if 0 <= r < N and 0 <= c < M and not board[r][c] and (r, c) not in e and not visited[r][c]:
                visited[r][c] = 1
                ans -= 1
                q.append((r, c))


dr = [-1, 0, 1, 0]              # 상 우 하 좌
dc = [0, 1, 0, -1]

N, M = map(int, sys.stdin.readline().split())                               # 세로, 가로 크기
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]    # 연구소 현황
empty_coordinates = []                          # 비어 있는 공간의 좌표들
start_coordinates = []                          # 바이러스 있는 공간의 좌표들
wall = set()                                    # 3곳의 벽을 세울 공간을 담을 변수
answer = 0                                      # 정답 변수

for i in range(N):                              # 연구실을 한번 전체 탐색하여
    for j in range(M):                          # 바이러스 있는 구역과 비어있는 구역의 좌표값을 따로 저장
        if board[i][j] == 2:
            start_coordinates.append((i, j))
        elif board[i][j] == 0:
            empty_coordinates.append((i, j))

safe = len(empty_coordinates) - 3               # 초기 안전한 구역의 개수 = 비어있는 공간의 개수 - 벽을 세울 3개의 공간
for e in combinations(empty_coordinates, 3):    # 벽을 세울 공간을 조합으로 구함
    visited = [[0] * M for _ in range(N)]       # 바이러스가 이미 침투했는지 확인을 위한 리스트
    ans = safe

    solution()
    
    answer = max(answer, ans)                   # 이전의 경우와 비교하여 현재 구한 안전구역의 개수 중 더 많은걸 저장

print(answer)