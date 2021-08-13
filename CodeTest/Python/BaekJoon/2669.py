import sys

board = [[0]*100 for _ in range(100)]                           # x, y의 값이 1이상 100이하이므로 2차원 배열 최대 크기가 100 * 100
answer = 0                                                      # 4개 사각형의 면적

for _ in range(4):  
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

    for i in range(x1, x2):
        for j in range(y1, y2):
            board[i-1][j-1] = 1                                 # 사각형 영역의 값을 1로 설정

for row in board:                                               # 행별로 값이 1인 부분의 갯수 카운트
    answer += row.count(1)

print(answer)