import sys

number = int(sys.stdin.readline())
num_list = []
num_dict = {}
my_sum = 0
max_cnt = 0
mode = []
mode_ans = 0

for _ in range(number):
    num = int(sys.stdin.readline())

    num_list.append(num)
    
    if num not in num_dict:
        num_dict[num] = 0
    num_dict[num] +=1 

    my_sum += num
num_list.sort()

# 오름차순으로 Sort 한번 / 딕셔너리 한번
avg = my_sum/number
cnt_val = num_list[number//2]

for k,v in num_dict.items():
    if max_cnt < v:
        mode = []
        max_cnt = v
        mode.append(k)
    elif max_cnt == v:
        mode.append(k)

if len(mode) > 1:
    mode = sorted(mode)[1]
else:
    mode = mode[0]

num_range = num_list[-1] - num_list[0]

print(f'{avg:0.0f}\n{cnt_val}\n{mode}\n{num_range}')