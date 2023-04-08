import sys
sys.stdin = open('input.txt')


def search(num):
    if num:
        nums.add(int(''.join(num)))

    for n in range(10):
        if int(num[-1]) <= n:
            continue
        search(num + [str(n)])


N = int(sys.stdin.readline())
nums = set()

for n in range(10):
    search([str(n)])

sorted_nums = list(sorted(nums))


print(-1 if len(sorted_nums) <= N else sorted_nums[N])
