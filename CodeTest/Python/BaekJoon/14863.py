import sys
sys.stdin = open('input.txt')


def sol(idx, remain):
    if remain < 0:
        return -1e10
    elif idx == N:
        return 0
    elif dp[idx][remain] != -1:
        return dp[idx][remain]

    dp[idx][remain] = max(sol(idx+1, remain - infos[idx][0]) + infos[idx]
                          [1], sol(idx+1, remain - infos[idx][2]) + infos[idx][3])
    return dp[idx][remain]


N, K = map(int, sys.stdin.readline().split())
dp = [[-1] * (K+1) for _ in range(N)]
infos = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

answer = sol(0, K)
print(answer)
