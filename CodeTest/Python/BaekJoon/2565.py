# https://namu.wiki/w/%EC%B5%9C%EC%9E%A5%20%EC%A6%9D%EA%B0%80%20%EB%B6%80%EB%B6%84%20%EC%88%98%EC%97%B4
import sys
from bisect import bisect_left
sys.stdin = open('input.txt')


def case1():
    dp = []
    for i in range(N):
        dp.append(1)
        for j in range(i):
            if right[j] < right[i]:
                dp[i] = max(dp[i], dp[j]+1)
    print(N - max(dp))


def case2():
    table = [[0], [0]]
    for i in range(N):
        idx = bisect_left(table[1], right[i])

        if len(table[0]) == idx:
            table[0].append(table[0][-1] + 1)
            table[1].append(right[i])
        else:
            table[1][idx] = right[i]

    print(N - table[0][-1])


N = int(sys.stdin.readline())
lines = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
left, right = zip(*sorted(lines, key=lambda x: x[0]))


# LIS (Longest Increasing Subsequence)
# case1. O(N^2)
case1()

# case2. O(NlogN)
case2()
