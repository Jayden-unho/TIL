import sys

num = int(sys.stdin.readline())
y_dict = {}
key_list = []

for _ in range(num):
    x,y = map(int, sys.stdin.readline().split())
    
    if y not in y_dict.keys():
        y_dict[y] = []
    y_dict[y].append(x)

key_list = sorted(list(y_dict.keys()))

for y in key_list:
    tmp = sorted(y_dict[y])
    for x in tmp:
        print(x, y)