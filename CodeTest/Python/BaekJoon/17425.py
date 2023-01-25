import sys
sys.stdin = open('input.txt')

N = 1000000
nums = [1] * (N+1)
nums[0] = 0

for i in range(2, N+1):
    for j in range(1, int(N/i+1)):
        nums[i*j] += i

for i in range(1, N+1):
    nums[i] = nums[i-1] + nums[i]

for _ in range(int(sys.stdin.readline())):
    print(nums[int(sys.stdin.readline())])
