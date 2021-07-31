import sys

n, x= map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    if x > a[i]:
        print(a[i], end=' ')