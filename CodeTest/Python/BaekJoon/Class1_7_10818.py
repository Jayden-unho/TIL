import sys

n, *num = map(int, sys.stdin.read().split())

print(min(num), max(num))