import sys
sys.stdin = open('input.txt')


N = int(input())
dp = [0] * N

dp[0] = int(input())
dp[1] = dp[0] + int(input())

for idx in range(2, N):
    num = int(input())
    dp[idx] = max(dp[idx-2] + num, dp[idx-1] + num)
    

print(dp)