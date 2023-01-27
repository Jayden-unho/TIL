import sys
sys.stdin = open('input.txt')

dr = [-1, 0, 1, 0]                                              # 위 오른쪽 아래 왼쪽
dc = [0, 1, 0, -1]


def sol(y, x):
    global answer

    answer = max(answer, len(visited))

    for k in range(4):
        r = y + dr[k]
        c = x + dc[k]

        if 0 <= r < R and 0 <= c < C and board[r][c] not in visited:
            visited.add(board[r][c])
            sol(r, c)
            visited.remove(board[r][c])


R, C = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
visited = set(board[0][0])
answer = len(visited)

sol(0, 0)

print(answer)
