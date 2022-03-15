import sys
from collections import deque
sys.setrecursionlimit(1000000)

dr = [1, 0, -1]     # 아래, 오른쪽, 왼쪽위
dc = [0, 1, -1]

def solution(n):
    answer = []                                                     # 정답 리스트
    pyramid = [[0] * n for _ in range(n)]                           # 2차원 배열
    direction = 0                                                   # 진행 방향, 초기 아래 방향
    
    def make_pyramid(y, x, direction, num):                         # 피라미드 생성
        if 0 <= y < n and 0 <= x < n and not pyramid[y][x]:         # 범위 안의 값이고, 숫자를 채우지 않았다면
            pyramid[y][x] = num                                     # 숫자 입력

            r = y + dr[direction]                                   # 다음 좌표
            c = x + dc[direction]

            if not (0 <= r < n and 0 <= c < n) or (pyramid[r][c]):  # 다음 좌표가 범위를 벗어나거나 숫자가 이미 있다면
                direction = (direction+1) % 3                       # 진행 방향을 변경
                r = y + dr[direction]                               # 새로운 다음 좌표
                c = x + dc[direction]

            make_pyramid(r, c, direction, num+1)                    # 재귀 탐색
    
    def make_answer():                                  # 정답 리스트 생성
        for i in range(n):                              # 2차원 배열 반복하며
            for j in range(n):          
                if pyramid[i][j]:                       # 숫자가 있는 경우에만, 리스트에 추가
                    answer.append(pyramid[i][j])
                else:                                   # 숫자가 없는 경우, 다음 행 탐색
                    break
    
    make_pyramid(0, 0, direction, 1)
    make_answer()
    
    return answer