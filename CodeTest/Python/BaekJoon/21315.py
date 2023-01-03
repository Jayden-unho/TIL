import sys
from math import log2, floor
sys.stdin = open('input.txt')


def sol(li, K):
    """
    카드 섞기

    @params
        - li - 섞기 이전의 카드 배치
        - K - K의 값

    @returns
        - li - 섞은 이후 카드 배치
    """
    end = N

    for i in range(1, K+2):
        idx = K - i + 1
        li = li[end-2**idx:end] + li[:end-2**idx] + li[end:]
        end = 2 ** idx

    return li


N = int(sys.stdin.readline())
result = list(map(int, sys.stdin.readline().split()))
max_k = floor(log2(N-1))

# 정답이 가능한 K의 조합들
for first in range(1, max_k+1):
    for second in range(1, max_k+1):
        res = sol(list(range(1, N+1)), first)   # 1차 섞기
        res = sol(res, second)                  # 2차 섞기
        if res == result:                       # 정답이라면 종료
            print(first, second)
            exit(0)
