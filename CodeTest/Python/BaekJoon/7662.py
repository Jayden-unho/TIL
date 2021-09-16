import sys
from collections import deque
sys.stdin = open('input.txt')


T = int(sys.stdin.readline())

for _ in range(T):
    command, num = map(str, sys.stdin.readline().split())
    num = int(num)

    low_q = deque()
    high_q = deque()

    if not low_q and not high_q and command == 'I':
        low_q.append(num)
    elif command == 'I':
        if not high_q:
            high_q.append(num)
        elif low_q[0] > num:
            low_q.appendleft(num)
            