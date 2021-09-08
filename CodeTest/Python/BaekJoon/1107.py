import sys
from collections import deque
sys.stdin = open('input.txt')



N = tmp_N = int(input())
M = int(input())
possible = [x for x in range(10)]
if M != 0:
    possible = sorted(list(set(possible).difference(map(int, input().split()))))
n_stack = []  # 앞에서부터 1의 자리
compare_down = deque()
compare_up = deque()
compare_list = []
answer = []

while tmp_N:
    n_stack.append(tmp_N%10)
    tmp_N //= 10

if possible:
    for idx in range(len(n_stack)-1, -1, -1):
        if n_stack[idx] in possible:
            compare_down.appendleft(n_stack[idx])
            compare_up.appendleft(n_stack[idx])
        else:
            tmp_up = possible[0]
            tmp_down = possible[-1]
            for k in range(len(possible)):    
                if n_stack[idx] > possible[k]:
                    tmp_up = possible[k]
                if n_stack[idx] < possible[k]:
                    tmp_down = possible[k]

            compare_down.appendleft(tmp_down)
            compare_up.appendleft(tmp_up)
            break
    # print(compare_down, compare_up)

    while len(compare_down) < len(n_stack):
        compare_down.appendleft(possible[-1])
        compare_up.appendleft(possible[0])


    tmp_up = 0
    tmp_down = 0
    a = 0
    if len(possible) > 1 and possible[0] == 0:
        b = str(possible[1])
    else:
        b = str(possible[0])

    for i in range(len(compare_down)):
        tmp_up += compare_up[i] * (10**i)
        tmp_down += compare_down[i] * (10**i)
        
        b += str(possible[0])
        if i < len(compare_down)-1:
            a += possible[-1] * (10**i)


    answer.append(abs(100-N))
    if a == 0:
        compare_list.extend([int(b), tmp_up, tmp_down])
    else:
        compare_list.extend([a, int(b), tmp_up, tmp_down])
    for e in compare_list:
        answer.append(len(str(e)) + abs(e-N))

    print(compare_list)
    print(answer)
    print(min(answer))
elif not possible:
    print(abs(100-N))