import sys
sys.setrecursionlimit(1000000)
sys.stdin = open('input.txt')

def solution(node):
    for next in linked[node]:
        if not distance[next]:
            distance[next] = distance[node] + 1
            solution(next)

N = int(sys.stdin.readline())
need_move = 0
linked = [[] for _ in range(N+1)]
distance = [0] * (N+1)

for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    linked[a].append(b)
    linked[b].append(a)

distance[0] = 1
solution(0)

for idx in range(2, N+1):
    if len(linked[idx]) == 1:
        need_move += distance[idx]

if need_move % 2:
    print('Yes')
else:
    print('No')