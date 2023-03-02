import sys
sys.stdin = open('input.txt')


def chk_valid(diff_y, diff_x):
    height, width = N1, M1

    for y, x in needs:
        ny, nx = y - diff_y, x - diff_x
        if 0 <= ny < N1 and 0 <= nx < M1:
            if board1[ny][nx] == 1:
                return 1e10
        else:
            if ny < 0 or ny >= N1:
                height = max(height, min(abs(ny-N1+1), abs(0-ny))+N1)
            if nx < 0 or nx >= M1:
                width = max(width, min(abs(nx-M1+1), abs(0-nx))+M1)

    return height * width


N1, M1 = map(int, sys.stdin.readline().split())
board1 = [list(map(int, list(sys.stdin.readline().rstrip())))
          for _ in range(N1)]
N2, M2 = map(int, sys.stdin.readline().split())
board = [list(map(int, list(sys.stdin.readline().rstrip())))
         for _ in range(N2)]
answer = min((N1+N2)*max(M1, M2), (N1+M2)*max(N2, M1))

empty = []
for i in range(N1):
    for j in range(M1):
        if board1[i][j] == 0:
            empty.append((i, j))


def ratation_board(board):
    return list(zip(*board))


def get_needs():
    needs = []
    R = len(board)
    C = len(board[0])

    for i in range(50, 50+R):
        for j in range(50, 50+C):
            if board[i-50][j-50] == 1:
                needs.append((i, j))
    return needs


for rotate in range(4):
    board = ratation_board(board[::-1])
    needs = get_needs()

    sy, sx = needs[0]
    for y, x in empty:
        diff_y, diff_x = sy-y, sx-x
        answer = min(answer, chk_valid(diff_y, diff_x))

print(answer)
