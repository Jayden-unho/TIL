"""
비트마스킹
"""

import sys
from itertools import combinations
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, 2):
    N = int(input())
    n_li = list(map(int, input().split()))
    a = 1

    for i in n_li:
        a |= a << i
    
    print('#{} {}'.format(tc, bin(a).count('1')))







    # for k in range(N+1):
    #     collect = set(combinations(n_li, k))
    #     # print('LOG --- TC : {} ___ COLLECT : {}'.format(tc, collect))

    #     for element in collect:
    #         answer.add(sum(element))