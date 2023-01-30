import sys
from collections import deque
sys.stdin = open('input.txt')


while True:
    N, K = map(int, sys.stdin.readline().split())
    if not N and not K:
        break

    nums = list(map(int, sys.stdin.readline().split()))
    parents = {}

    nodes = deque([nums[0]])
    for i in range(1, N):
        num = nums[i]
        nodes.append(num)

        if nums[i-1]+1 != num:
            node = nodes.popleft()
        parents[num] = node

    answer = 0
    for i in range(1, N):
        num = nums[i]
        if parents[num] != parents[K] and parents.get(parents[num], 0) == parents.get(parents[K], 0):
            answer += 1

    print(answer)
