import sys
sys.stdin = open('input.txt')

N, K = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
answer = 0
cnts = {}

ans = 0
l, r = 0, 0
while r < N:
    if cnts.get(nums[r], 0) < K:
        cnts[nums[r]] = cnts.get(nums[r], 0) + 1
        r += 1
        ans += 1
    else:
        cnts[nums[l]] -= 1
        l += 1
        ans -= 1

    answer = max(answer, ans)

print(answer)
