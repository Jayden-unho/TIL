import sys
sys.stdin = open('input.txt')

dr = [-1, -1, 1, 1]     # 왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래
dc = [-1, 1, -1, 1]

impossible_dict = {}

def set_impossible_dict(y: int, x: int) -> None:
    impossible_dict[(y, x)] = get_impossible(y, x)

def get_impossible(y: int, x: int) -> set:
    impossible = set([(y, x)])
    stack = [(y, x, 0), (y, x, 1), (y, x, 2), (y, x, 3)]

    while stack:
        y, x, d = stack.pop()
        
        r = y + dr[d]
        c = x + dc[d]

        if 0 <= r < N and 0 <= c < N:
            if board[r][c] == 2:
                return {}
            elif board[r][c] == 1:
                impossible.add((r, c))
            stack.append((r, c, d))
    return impossible

def solution(idx, ans, bishop):
    global answer

    if idx == possible_length:
        if answer < ans:
            print(bishop)
        answer = max(answer, ans)
        return

    for i in range(idx, possible_length):
        y, x = possible[i]
        
        for by, bx in bishop:
            if (y, x) in impossible_dict[(by, bx)]:
                break
        else:
            solution(i+1, ans+1, bishop + [(y, x)])
    solution(possible_length, ans, bishop)
        
N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
possible = []
answer = 0

for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            possible.append((i, j))
            set_impossible_dict(i, j)
possible_length = len(possible)
max_can = [0] * possible_length

solution(0, 0, [])

print(answer)