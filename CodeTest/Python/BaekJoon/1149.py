import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
li = []
dp = [[-1, -1] for _ in range(N)]
idx = [-1] * N

for _ in range(N):
    r, g, b = map(int, sys.stdin.readline().split())
    li.append((r, g, b))

tmp_v = min(li[0])
tmp_idx = li[0].index(tmp_v)
dp[0] = [tmp_v, tmp_idx]

for i in range(1, N):
    pre_idx = dp[i-1][1]
    first = dp[i-1][0] + min(li[i][(pre_idx+1)%3], li[i][(pre_idx+2)%3])
    
    second_v = min(li[i])
    second_idx = li[i].index(second_v)
    second = second_v + min(li[i-1][(second_idx+1)%3], li[i-1][(second_idx+2)%3])