import sys

num = list(map(int, sys.stdin.read().split()))

print("{0}\n{1}".format(max(num), num.index(num)+1))