import sys
from collections import deque
sys.stdin = open('input.txt')

N, K = map(int, sys.stdin.readline().split())

dp = {}
dp[N] = 1

if N >= K:
    print(N - K)
    print(*range(N, K-1, -1))
else:
    q = deque([(N, [N])])
    max_arrage = max(K + K//2, N)
    while True:
        node, paths = q.popleft()
        if node == K:
            print(dp[node]-1)
            print(*paths)
            break

        for num in [node, -1, 1]:
            next_node = node + num
            next_distance = dp[node] + 1
            if not dp.get(next_node, False) and 0 <= next_node <= max_arrage:
                dp[next_node] = next_distance
                q.append((next_node, paths + [next_node]))
