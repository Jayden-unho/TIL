import sys
sys.stdin = open('input.txt')


def solution(idx, red, blue):
    global answer

    if idx >= answer:
        return
    if blue == hole:
        return
    elif red == hole:
        answer = idx
        return


    for k in range(4):
        rr = red[0] + dr[k]
        rc = red[1] + dc[k]

        br = blue[0] + dr[k]
        bc = blue[0] + dc[k]
        
        n_red = red[:]
        n_blue = blue[:]

        if 0 <= rr < N and 0 <= rc < M:
            if board[rr][rc] == '.':
                n_red = [rr, rc]
                if 0 <= br < N and 0 <= bc < M and board[br][bc] == '.':
                    n_blue = [br, bc]

            elif board[rr][rc] == 'B':
                if 0 <= br < N and 0 <= bc < M and board[br][bc] == '.':
                    n_blue = [br, bc]
                    n_red = [rr, rc]
            
            elif board[rr][rc] == '#':
                if 0 <= br < N and 0 <= bc < M and board[br][bc] == '.':
                    n_blue = [br, bc]
        else:
            print(rr, rc)
            
        solution(idx+1, n_red, n_blue)


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

N, M = map(int, sys.stdin.readline().split())           # height / width
board = [list(input()) for _ in range(N)]
print(board)
red = []
blue = []
hole = []
answer = 11

for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            red = [i, j]
        elif board[i][j] == 'B':
            blue = [i, j]
        elif board[i][j] == '0':
            hole = [i, j]

for k in range(4):
    solution(0, red, blue)

if answer > 10:
    answer = -1
print(answer)