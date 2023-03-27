"""
https://peisea0830.tistory.com/116
"""
import sys
sys.setrecursionlimit(100000000)
sys.stdin = open('input.txt')


def sol(idx, cnt):
    if idx >= N:
        return 0
    elif cnt >= 3:
        return 1
    elif dp[idx][cnt]:
        return dp[idx][cnt]

    if acc[idx] == target * (cnt+1):
        dp[idx][cnt] += sol(idx+1, cnt+1)
    dp[idx][cnt] += sol(idx+1, cnt)

    return dp[idx][cnt]


N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
acc = [0]

for n in nums:
    acc.append(acc[-1]+n)
acc = acc[1:]

if acc[-1] % 4:
    print(0)
else:
    target = acc[-1] // 4
    dp = [[0] * 4 for _ in range(N)]
    print(sol(0, 0))
