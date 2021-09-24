'''
시간초과
'''

import sys
from collections import deque
sys.stdin = open('input.txt')


T = int(sys.stdin.readline())

for _ in range(T):
    K = int(sys.stdin.readline())
    low_q = deque([])
    high_q = deque([])

    for _ in range(K):
        command, num = sys.stdin.readline().split()
        num = int(num)

        if command == 'I':
            while True:
                if low_q and low_q[-1] > num:
                    high_q.append(low_q.pop())
                elif high_q and high_q[-1] < num:
                    low_q.append(high_q.pop())
                else:
                    low_q.append(num)
                    break

        elif command == 'D':
            if num == -1:
                if low_q:
                    low_q.popleft()
                elif high_q:
                    high_q.pop()
            elif num == 1:
                if high_q:
                    high_q.popleft()
                elif low_q:
                    low_q.pop()


    if not low_q and not high_q:
        print('EMPTY')
    elif not low_q:
        print(high_q[0], high_q[-1])
    elif not high_q:
        print(low_q[-1], low_q[0])
    else:
        print(high_q[0], low_q[0])