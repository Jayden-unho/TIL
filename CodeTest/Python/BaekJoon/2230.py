import sys
sys.stdin = open('input.txt')


N, M = map(int, sys.stdin.readline().split())
nums = list(sorted([int(sys.stdin.readline()) for _ in range(N)]))

answer = 1e10
l, r = 0, 1

while r < N:
    if answer == M:
        break

    num = nums[r] - nums[l]
    if num >= M:
        answer = min(num, answer)
        l += 1
    else:
        r += 1

print(answer)
