import sys
sys.stdin = open('input.txt')

def get_can_num(y, x):                              # 행, 열, 사각형을 확인해서 들어갈 수 있는 번호 구하기
    can_num = {1, 2, 3, 4, 5, 6, 7, 8, 9}.difference(sudoku[y])     # 현재 행에서 들어갈 수 있는 번호

    for j in range(9):                              # 현재 열에서 들어갈 수 있는 번호
        if sudoku[j][x] in can_num:
            can_num.remove(sudoku[j][x])

    r = y//3 * 3
    c = x//3 * 3
    for i in range(r, r+3):                         # 현재 사각형에서 들어갈 수 있는 번호
        for j in range(c, c+3):
            if sudoku[i][j] in can_num:
                can_num.remove(sudoku[i][j])
    
    return can_num

def solution(n):
    if n == N:                      # 모든 번호를 찾았다면
        for i in range(9):          # 출력
            print(*sudoku[i])
        sys.exit(0)                 # 정답 한번 찾았으면 다음 탐색하지 않고 프로그램 종료

    y, x = coor[n]                  # 빈칸의 좌표
    for num in get_can_num(y, x):   # 해당 좌표에서 들어갈 수 있는 숫자들 넣어보기
        sudoku[y][x] = num          # 숫자 입력
        solution(n+1)               # 다음 좌표 탐색
        sudoku[y][x] = 0            # 불가능한 경우, 다시 빈칸


sudoku = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]   # 주어진 입력
coor = []                                                                   # 빈칸인 좌표들

for i in range(9):
    for j in range(9):
        if not sudoku[i][j]:        # 빈칸 좌표
            coor.append((i, j))

N = len(coor)                       # 빈칸의 개수
solution(0)                         # 탐색