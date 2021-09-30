import sys
from itertools import permutations
sys.stdin = open('input.txt')


# def solution(plus, minus, multi, div, ans, idx):
#     global max_ans, min_ans

#     if idx >= N:
#         if max_ans < ans:
#             max_ans = ans
#         if min_ans > ans:
#             min_ans = ans
#         return
#     elif not plus and not multi and ans < max_ans:
#         return
#     elif not minus and ans > min_ans:
#         return
    
#     for _ in range(4):
#         if plus > 0:
#             solution(plus-1, minus, multi, div, ans+num_li[idx], idx+1)
#         if minus > 0:
#             solution(plus, minus-1, multi, div, ans-num_li[idx], idx+1)
#         if multi > 0:
#             solution(plus, minus, multi-1, div, ans*num_li[idx], idx+1)
#         if div > 0:
#             solution(plus, minus, multi, div-1, int(ans/num_li[idx]), idx+1)
            

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    op_cnt = list(map(int, input().split()))
    num_li = list(map(int, input().split()))

    max_ans = -1e10
    min_ans = 1e10

    op_li = ([1] * op_cnt[0]) + ([2] * op_cnt[1]) + ([3] * op_cnt[2]) + ([4] * op_cnt[3])
    comb = set(permutations(op_li, N-1))

    for e in comb:
        tmp_ans = num_li[0]
        for i in range(N-1):
            if e[i] == 1:
                tmp_ans += num_li[i+1]
            elif e[i] == 2:
                tmp_ans -= num_li[i+1]
            elif e[i] == 3:
                tmp_ans *= num_li[i+1]
            elif e[i] == 4:
                tmp_ans = int(tmp_ans/num_li[i+1])

        if tmp_ans > max_ans:
            max_ans = tmp_ans
        if tmp_ans < min_ans:
            min_ans = tmp_ans

    print('#{} {}'.format(tc, max_ans - min_ans))




    # solution(op_cnt[0], op_cnt[1], op_cnt[2], op_cnt[3], num_li[0], 1)