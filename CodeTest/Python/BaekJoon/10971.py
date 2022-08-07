import sys
sys.stdin = open('input.txt')


def solution(start, visited):
    if dp.get((start, visited), False):
        return dp[(start, visited)]
    elif visited == (1 << N) - 1:
        dp[(start, 0)] = prices[start][0]
        return dp[(start, 0)]

    for i in range(1, N):
        if prices[start][i] and not (visited & 1 << i):
            dp[(start, visited)] = min(dp.get((start, visited), 1e10), solution(
                i, visited | 1 << i) + prices[start][i])
    return dp[(start, visited)]


N = int(sys.stdin.readline())
prices = [list(map(lambda x: 1e10 if x == '0' else int(
    x), sys.stdin.readline().split())) for _ in range(N)]
dp = {}

print(solution(0, 1))
