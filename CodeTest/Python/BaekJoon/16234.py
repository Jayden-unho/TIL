"""
시간 초과 - ...?
pypy3 로는 통과

Memory - 175852 kb 
Time - 2332ms
"""


import sys
from collections import deque
sys.setrecursionlimit(10000)


def check(y, x, num):               # 같은 연합끼리 체크
    q = deque([(y, x)])
    union[y][x] = num

    while q:
        node = q.popleft()

        for k in range(4):
            r = node[0] + dr[k]
            c = node[1] + dc[k]

            if 0 <= r < N and 0 <= c < N and not union[r][c] and L <= abs(board[r][c] - board[node[0]][node[1]]) <= R:
                union[r][c] = num
                union_num[num][0] += board[r][c]
                union_num[num][1] += 1
                q.append((r, c))
            

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

N, L, R = map(int, sys.stdin.readline().split())                            # 땅 크기 / 최소이상 최대이하
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]    # 각 나라 인구수
union_num = {}                              # 연합 번호별 인구수, 연합국 개수 카운트
hour = 0


while True:
    union = [[0]*N for _ in range(N)]           # 연합 맵으로 보여짐 (초기화 연속으로 시간 증가)

    num = 1
    for i in range(N):                                  # 연합끼리 국경 열기
        for j in range(N):
            if not union[i][j]:                         # 연합 없으면 생성
                union_num[num] = [board[i][j], 1]
                check(i, j, num)
                union_num[num] = union_num[num][0] // union_num[num][1]
                num += 1

            board[i][j] = union_num[union[i][j]]                            # 연합인땅 인구 재배치
            
    if len(union_num.keys()) == N*N:
        break
    else:
        hour += 1

print(hour)