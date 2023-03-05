import sys
from collections import deque
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
nums = enumerate(list(map(int, sys.stdin.readline().split())), start=1)

answer = []
q = deque()
q.extend(nums)

while q:
    idx, v = q.popleft()

    answer.append(idx)

    if v > 0:
        v -= 1

    while True:
        if v == 0 or not q:
            break

        if v < 0:
            n = q.pop()
            q.appendleft(n)
            v += 1
        else:
            n = q.popleft()
            q.append(n)
            v -= 1


print(*answer)
