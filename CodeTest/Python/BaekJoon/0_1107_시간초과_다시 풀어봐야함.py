import sys
from itertools import product
sys.stdin = open('input.txt')

N = int(input())
M = int(input())
len_N = len(str(N))
possible = [x for x in range(10)]
answer = abs(100-N)

if M:
    possible = sorted(list(set(possible).difference(map(int, input().split()))))


A = list(set(product(possible, repeat=len_N))) + list(set(product(possible, repeat=len_N-1))) + list(set(product(possible, repeat=len_N+1)))


for e in A:
    if e == ():
        continue

    tmp_answer = 0
    tmp_num = 0
    
    for idx in range(len(e)):
        tmp_num += e[idx] * (10**idx)
    
    tmp_answer = len(e) + abs(tmp_num - N)
    if tmp_answer < answer:
        answer = tmp_answer

print(answer)