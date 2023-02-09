import sys
sys.stdin = open('input.txt')


def is_good(i):
    target = nums[i]
    for j in range(N):
        if i == j:
            continue

        left, right = nums[j], target - nums[j]
        if target == left and target == right:
            if cnts.get(target, 0) >= 2:
                return True
        elif left == right:
            if cnts.get(left, 0) >= 2:
                return True
        else:
            if cnts.get(left, 0) >= 1 and cnts.get(right, 0) >= 1:
                return True
    return False


N = int(sys.stdin.readline())
nums = list(sorted(map(int, sys.stdin.readline().split())))

cnts = {}
answer = 0

for n in nums:
    cnts[n] = cnts.get(n, 0) + 1

for i in range(N):
    cnts[nums[i]] -= 1
    if is_good(i):
        answer += 1
    cnts[nums[i]] += 1

print(answer)
