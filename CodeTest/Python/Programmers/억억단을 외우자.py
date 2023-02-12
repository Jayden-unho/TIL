"""
1번 TestCase - 런터임 에러 (배열 크기 초과 예상)
10번 TestCase - 시간초과
"""

import sys
from math import ceil, log2
sys.setrecursionlimit(100000000)


def solution(e, starts):
    def get_common_divisions(e):
        for num in range(2, e+1):
            cds[num] += 1
            for j in range(num, e//num+1):
                if num == j:
                    cds[num**2] += 1
                    continue
                cds[num * j] += 2

    def init_segment_tree(node, left, right):
        if left == right:
            segment_tree[node] = (cds[left], left)
            return segment_tree[node]
        elif left > right:
            print('?')

        mid = (left+right) // 2
        l = init_segment_tree(node*2, left, mid)
        r = init_segment_tree(node*2+1, mid+1, right)

        ans = (-1, -1)
        if l[0] > r[0]:
            ans = l
        elif l[0] < r[0]:
            ans = r
        elif l[1] >= r[1]:
            ans = r
        elif l[1] < r[1]:
            ans = l

        segment_tree[node] = ans
        return segment_tree[node]

    def find_ans(node, left, right, target_left, target_right):
        if target_right < left or right < target_left:
            return (-1, -1)
        elif target_left <= left and right <= target_right:
            return segment_tree[node]

        mid = (left+right) // 2
        l = find_ans(node*2, left, mid, target_left, target_right)
        r = find_ans(node*2+1, mid+1, right, target_left, target_right)

        if l[0] > r[0]:
            return l
        elif l[0] < r[0]:
            return r
        elif l[1] >= r[1]:
            return r
        elif l[1] < r[1]:
            return l

    answer = []
    cds = [1] * (e+1)
    min_s = min(starts)
    segment_tree = [(-1, -1) for _ in range(2**ceil(log2(e-min_s)) * 2)]

    get_common_divisions(e)
    init_segment_tree(1, min_s, e)

    for s in starts:
        ans = find_ans(1, min_s, e, s, e)
        answer.append(ans[1])

    return answer


print(solution(8, [1, 3, 7]))
print(solution(5000000, [31] * 100000))
