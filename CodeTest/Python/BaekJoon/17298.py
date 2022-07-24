import sys
from collections import deque
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
stack = []
answers = deque()

for i in range(N-1, -1, -1):
    while True:
        if stack:
            num = stack.pop()
            if num > arr[i]:
                answers.appendleft(num)
                stack.append(num)
            else:
                continue
        else:
            answers.appendleft(-1)
        stack.append(arr[i])
        break

print(*answers)