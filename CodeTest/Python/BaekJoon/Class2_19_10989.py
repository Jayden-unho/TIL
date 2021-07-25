import sys

n = int(sys.stdin.readline())
num_dict = {}

for i in range(1, 10001):
    num_dict[i] = 0

for _ in range(n):
    num = int(sys.stdin.readline())
    num_dict[num] += 1

for k,v in num_dict.items():
    for _ in range(v):
        print(k)