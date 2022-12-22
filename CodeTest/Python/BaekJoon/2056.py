import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
linked = [[] for _ in range(N)]
delays = []
needs = []
dp = [0] * N
q = []

for idx in range(N):
    need_time, M, *nums = map(int, sys.stdin.readline().split())
    delays.append(need_time)
    needs.append(M)

    if M:
        for n in nums:
            linked[n-1].append(idx)
    else:
        q.append(idx)
        dp[idx] = need_time

while q:
    node = q.pop()
    for next in linked[node]:
        dp[next] = max(dp[node] + delays[next], dp[next])
        needs[next] -= 1

        if not needs[next]:
            q.append(next)

print(max(dp))
