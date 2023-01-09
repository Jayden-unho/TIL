import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
costs = [[0] * N for _ in range(N)]

for i in range(1, N):
    costs[i][0] = costs[i-1][0] + max(board[i][0] - board[i-1][0] + 1, 0)
    costs[0][i] = costs[0][i-1] + max(board[0][i] - board[0][i-1] + 1, 0)

for i in range(1, N):
    for j in range(1, N):
        y_diff = max(board[i][j] - board[i-1][j] + 1, 0)
        x_diff = max(board[i][j] - board[i][j-1] + 1, 0)
        costs[i][j] = min(costs[i-1][j] + y_diff, costs[i][j-1] + x_diff)

print(costs[-1][-1])
