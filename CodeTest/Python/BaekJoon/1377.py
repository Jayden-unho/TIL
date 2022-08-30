import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
sorted_nums = list(sorted(
    enumerate([int(sys.stdin.readline()) for _ in range(N)], 1), key=lambda x: x[1]))

answer = -1
for cur_idx in range(N):
    pre_idx = sorted_nums[cur_idx][0]
    answer = max(answer, pre_idx - cur_idx)

print(answer)
