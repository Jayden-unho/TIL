import sys
sys.stdin = open('input.txt')


def get_min_cost():
    for i in range(1, sum_costs+1):
        for j in range(1, N+1):
            if costs[j] > i:
                dp[i][j] = dp[i][j-1]
            else:
                dp[i][j] = max(dp[i][j-1], memories[j] + dp[i-costs[j]][j-1])

            if dp[i][j] >= M:
                return i
    return 0


N, M = map(int, sys.stdin.readline().split())
memories = [0] + list(map(int, sys.stdin.readline().split()))
costs = [0] + list(map(int, sys.stdin.readline().split()))
sum_costs = sum(costs)
dp = [[0] * (N+1) for _ in range(sum_costs+1)]

print(get_min_cost())
