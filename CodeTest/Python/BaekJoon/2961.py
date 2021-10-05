""" bit masking / powerset /  """

import sys
sys.stdin = open('input.txt')


N = int(input())
ingredient = [tuple(map(int, input().split())) for _ in range(N)]
answer = 1e10


for i in range(1, 1 << N):
    tmp, B = 1, 1
    for j in range(N):
        if i & (1 << j):
            tmp *= ingredient[j][0]
            B = B << ingredient[j][1]

    S = 1 << tmp
    ans = abs(len(bin(B)) - len(bin(S)))
    
    if answer > ans:
        answer = ans

print(answer)