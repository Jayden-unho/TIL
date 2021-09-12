import sys


N = int(sys.stdin.readline())
li = [0] + list(map(int, sys.stdin.readline().split()))

for idx in range(1, len(li)):               # accumulate list
    li[idx] = li[idx-1] + li[idx]

M = int(sys.stdin.readline())
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())

    print(li[j] - li[i-1])