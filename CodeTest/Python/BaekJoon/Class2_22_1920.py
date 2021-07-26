import sys

number = int(sys.stdin.readline())
num_dict = {}
number_list = list(map(int, sys.stdin.readline().split()))

for e in number_list:
    num_dict[e] = 1

repeat = int(sys.stdin.readline())
repeat_num_list = list(map(int, sys.stdin.readline().split()))

for i in repeat_num_list:
    if i in num_dict:
        print(1)
    else:
        print(0)