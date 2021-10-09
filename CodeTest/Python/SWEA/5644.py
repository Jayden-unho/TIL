import sys
from collections import deque
import os
import time
from pprint import pprint
sys.stdin = open('input.txt')


def bfs(y, x, coverage, performace, num):      # 좌표 / 남은 충전 범위 / 충전 성능 / BC 이름
    visited = [[0] * 10 for _ in range(10)]

    q = deque([(y, x)])
    board[y][x] += [(num, performace)]          # 해당 좌표에 어떤 BC 이고, 성능인지 튜플로 담김
    visited[y][x] = 1

    while q:
        node = q.popleft()

        for k in range(1, 5):
    
            r = node[0] + dr[k]
            c = node[1] + dc[k]

            if 0 <= r < 10 and 0 <= c < 10 and not visited[r][c]:       
                if visited[node[0]][node[1]] == coverage:               # 설정된 영영에 도착하면 종료
                    return

                visited[r][c] = visited[node[0]][node[1]] + 1
                board[r][c] += [(num, performace)]
                q.append((r, c))


dr = [0, -1, 0, 1, 0]       # 이동 - 이동하지 않음 / 상 / 우 / 하 / 좌 
dc = [0, 0, 1, 0, -1]

T = int(input())
answer = []

for tc in range(1, T+1):
    M, A = map(int, input().split())        # 이동 시간 / BC 개수
    board = [[[] for _ in range(10)] for _ in range(10)]

    move_A = tuple(map(int, input().split()))       # 사용자 이동 정보 (0-이동x, 1-상, 2-우, 3-하, 4-좌)
    move_B = tuple(map(int, input().split()))

    location_A = [0, 0]                 # 사용자별 위치
    location_B = [9, 9]

    charge_A = board[0][0]              # 사용자별 충전량 (초기 위치에서 충전 상태)
    charge_B = board[9][9]

    for idx in range(A):
        x, y, C, P = map(int, input().split())      # BC 좌표 / 충전 범위 / 충전량
        bfs(y-1, x-1, C+1, P, idx)                  # 충전 정보 저장
    
    for idx in range(M):
        location_A[0] = location_A[0] + dr[move_A[idx]]
        location_A[1] = location_A[1] + dc[move_A[idx]]

        location_B[0] = location_B[0] + dr[move_B[idx]]
        location_B[1] = location_B[1] + dc[move_B[idx]]

        if 