import sys
from collections import deque
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

answer = [[0] * (N+1) for _ in range(N+1)]
linked = [[] for _ in range(N+1)]
needs = [0] * (N+1)

for _ in range(M):
    X, Y, K = map(int, sys.stdin.readline().split())
    linked[Y].append((X, K))
    needs[X] += 1

q = deque()
default = set()
for i in range(1, N+1):
    if not needs[i]:
        q.append(i)
        default.add(i)

while q:
    node = q.popleft()
    for next_node, next_cnt in linked[node]:
        if node in default:
            answer[next_node][node] += next_cnt
        else:
            for k in range(1, N+1):
                answer[next_node][k] += next_cnt * answer[node][k]

        needs[next_node] -= 1
        if not needs[next_node]:
            q.append(next_node)

for i in range(1, N+1):
    if answer[N][i]:
        print(f'{i} {answer[N][i]}')
