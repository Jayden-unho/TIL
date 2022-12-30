import sys
sys.stdin = open('input.txt')

for _ in range(int(sys.stdin.readline())):
    N = int(sys.stdin.readline())
    values = list(map(int, sys.stdin.readline().split()))
    target = int(sys.stdin.readline())
    dp = [[0] * (target+1) for _ in range(N+1)]
    dp[0][0] = 1

    for i in range(1, N+1):
        for j in range(target+1):
            value = values[i-1]
            dp[i][j] = dp[i-1][j] + (dp[i][j-value] if j >= value else 0)

    print(dp[-1][-1])
