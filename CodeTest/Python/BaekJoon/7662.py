import sys
from collections import deque
sys.stdin = open('input.txt')


T = int(sys.stdin.readline())

for _ in range(T):
    K = int(sys.stdin.readline())
    q_min = deque()     # min
    q_max = deque()     # max

    for _ in range(K):
        command, num = map(str, sys.stdin.readline().split())
        
        if not q:
            if command == 'I':
                q.append(int(num))
        elif q:
            num = int(num)
            if command == 'I':
                for idx in range(len(q)):
                    if q[idx] > num:
                        q.insert(idx, num)
                        break
                    elif idx == len(q) - 1 and q[idx] < num:
                        q.append(num)
                        break
            elif num == -1:
                q.popleft()
            elif num == 1:
                q.pop()
    
    if not q:
        print('EMPTY')
    else:
        print(q[-1], q[0])