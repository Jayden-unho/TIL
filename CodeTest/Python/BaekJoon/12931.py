import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
total = sum(nums)
answer = 0

while total:
    is_divid = False
    for i in range(N):
        if not nums[i]:
            continue

        if nums[i] % 2:
            answer += 1
            total -= 1
            nums[i] -= 1

        if nums[i]:
            nums[i] //= 2
            total -= nums[i]
            is_divid = True

    if is_divid:
        answer += 1

print(answer)
