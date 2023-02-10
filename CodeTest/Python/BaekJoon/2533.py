import sys
sys.setrecursionlimit(100000000)
sys.stdin = open('input.txt')


def sol(node):
    visited[node] = 1

    for next_node in linked[node]:
        if not visited[next_node]:
            sol(next_node)
            dp[node][0] += dp[next_node][1]
            dp[node][1] += min(dp[next_node][0], dp[next_node][1])


N = int(sys.stdin.readline())
linked = [[] for _ in range(N)]
dp = [[0, 1] for _ in range(N)]
visited = [0] * N

for _ in range(N-1):
    u, v = map(lambda x: int(x)-1, sys.stdin.readline().split())
    linked[u].append((v))
    linked[v].append((u))

sol(0)

print(min(dp[0][0], dp[0][1]))
