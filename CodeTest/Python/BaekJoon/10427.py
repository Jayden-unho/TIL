import sys
from functools import reduce
sys.stdin = open('input.txt')

# 테스트 케이스 수
T = int(sys.stdin.readline())

for _ in range(T):
    N, *nums = map(int, sys.stdin.readline().split())
    sorted_nums = sorted(nums)
    # 구간합을 위한 누적합
    acc_nums = reduce(lambda p, c: p + [p[-1] + c], sorted_nums, [0])
    answer = 0

    # 2개부터 N개까지, S(2) ~ S(N)
    for k in range(2, N+1):
        min_num = 1e10

        # 시작 인덱스를 돌며, 구간들의 차이가 최소가 되는거 구하기
        for idx in range(N-k+1):
            num = sorted_nums[idx+k-1]
            prefix_sum = acc_nums[idx+k] - acc_nums[idx]
            min_num = min(min_num, num*k-prefix_sum)
        answer += min_num

    print(answer)
