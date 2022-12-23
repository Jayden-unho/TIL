import sys
sys.setrecursionlimit(1000000)
sys.stdin = open('input.txt')


def sol(node):
    visited[node] = 1
    for next in linked[node]:
        if not visited[next]:
            visited[node] += sol(next)

    return visited[node]


N, R, Q = map(int, sys.stdin.readline().split())
linked = [[] for _ in range(N)]
visited = [0] * N

for _ in range(N-1):
    u, v = map(lambda x: int(x)-1, sys.stdin.readline().split())
    linked[u].append(v)
    linked[v].append(u)

sol(R-1)

for _ in range(Q):
    q = int(sys.stdin.readline())
    print(visited[q-1])
