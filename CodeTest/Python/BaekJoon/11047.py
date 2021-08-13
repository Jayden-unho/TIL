import sys


n, k = map(int, sys.stdin.readline().split())
answer = 0
value = []

for _ in range(n):
    value.append(int(sys.stdin.readline()))
value.reverse()

for v in value:
    answer += k//v
    k %= v

print(answer)