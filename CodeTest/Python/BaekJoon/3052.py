import sys

def remainder(num):
    return int(num)%42

list_set = set(map(remainder, sys.stdin.read().split()))

print(len(list_set))