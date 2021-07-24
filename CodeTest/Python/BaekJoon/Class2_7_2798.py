import sys

n,m = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
max_num = 0

for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            num_sum = num_list[i] + num_list[j] + num_list[k]
            if(num_sum <= m and max_num < num_sum):
                max_num = num_sum

print(max_num)