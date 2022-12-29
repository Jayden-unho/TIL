import sys
sys.stdin = open('input.txt')


def set_palindrome(left, right):
    half_length = (right-left) // 2
    l, r = left + half_length, right - half_length

    prev = 1
    while l >= left:
        if prev and nums[l] == nums[r]:
            dp[l][r] = 1
        else:
            dp[l][r] = 0
            prev = 0

        l -= 1
        r += 1


N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
dp = [[-1] * N for _ in range(N)]

for _ in range(int(sys.stdin.readline())):
    S, E = map(lambda x: int(x)-1, sys.stdin.readline().split())

    if dp[S][E] != -1:
        print(dp[S][E])
        continue

    set_palindrome(S, E)
    print(dp[S][E])
