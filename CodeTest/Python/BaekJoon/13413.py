import sys
from collections import deque
sys.stdin = open('input.txt')

T = int(sys.stdin.readline())

for _ in range(T):
    L = int(sys.stdin.readline())

    start = sys.stdin.readline().rstrip()
    target = sys.stdin.readline().rstrip()

    white = 0
    black = 0

    for s, t in zip(start, target):
        if s == t:
            continue

        if t == 'W':
            white += 1
        if t == 'B':
            black += 1

    answer = min(white, black) + abs(white - black)
    print(answer)
