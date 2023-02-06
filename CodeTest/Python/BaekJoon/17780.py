import sys
sys.stdin = open('input.txt')


def update_pieces(y, x):
    for num in coors[(y, x)]:
        pieces[num][0] = y
        pieces[num][1] = x


def change_direction(d):
    if d in {0, 2}:
        return d+1
    else:
        return d-1


def get_new_coors(y, x, d):
    return y+dr[d], x+dc[d]


def chk_condition(y, x):
    if len(coors[(y, x)]) >= 4:
        return True
    return False


def combine_pieces(r, c, li):
    coors[(r, c)] = coors.get((r, c), []) + li


def solution():
    global answer

    while answer <= 1000:
        answer += 1

        for num in range(K):
            y, x, d = pieces[num]
            if coors[(y, x)][0] != num:
                continue

            r, c = get_new_coors(y, x, d)

            if not 0 <= r < N or not 0 <= c < N or board[r][c] == 2:
                d = change_direction(d)
                pieces[num][2] = d
                r, c = get_new_coors(y, x, d)

            if 0 <= r < N and 0 <= c < N and board[r][c] != 2:
                combine_pieces(r, c, coors[(y, x)][::-1]
                               if board[r][c] else coors[(y, x)])
                coors[(y, x)].clear()
                update_pieces(r, c)
                if chk_condition(r, c):
                    return


dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

N, K = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer = 0
coors = {}
pieces = {}

for idx in range(K):
    y, x, d = map(lambda x: int(x)-1, sys.stdin.readline().split())
    coors[(y, x)] = coors.get((y, x), []) + [idx]
    pieces[idx] = [y, x, d]

solution()

print(answer if answer <= 1000 else -1)
