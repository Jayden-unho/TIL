import sys

num_list = list(map(int, sys.stdin.readline().split()))
count = 0

for i in range(1,len(num_list)):
    if num_list[i] == num_list[i-1]+1:
        count += 1
    elif num_list[i] == num_list[i-1]-1:
        count -= 1

if count == 7:
    print('ascending')
elif count == -7:
    print('descending')
else:
    print('mixed')