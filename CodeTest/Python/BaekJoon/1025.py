import sys
sys.stdin = open('input.txt')


def is_square_num(num):
    return int(num ** 0.5) ** 2 == num


def sol(y, x, y_gap, x_gap, visited, nums):
    global answer

    if nums:
        num = int(''.join(nums))
        if is_square_num(num):
            answer = max(answer, num)

    if (y, x) in visited or not (0 <= y < N and 0 <= x < M):
        return

    sol(y+y_gap, x+x_gap, y_gap, x_gap,
        visited | {(y, x)}, nums + [board[y][x]])


N, M = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
answer = -1

for y in range(N):
    for x in range(M):
        for y_gap in range(-y, N-y):
            for x_gap in range(-x, M-x):
                sol(y, x, y_gap, x_gap, set(), [])

print(answer)
