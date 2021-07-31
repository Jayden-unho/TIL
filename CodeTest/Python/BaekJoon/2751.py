import sys

n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.read().split()))
num_list = sorted(num_list)

for i in range(len(num_list)):
    print(num_list[i])