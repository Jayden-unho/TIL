import sys

n, num = map(int, sys.stdin.read().split())
answer = 0

for _ in range(n):
    answer += num%10
    num //= 10

print(answer)