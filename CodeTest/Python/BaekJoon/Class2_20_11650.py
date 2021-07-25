#1
import sys

number = int(sys.stdin.readline())
x_dict = {}

for _ in range(number):
    x,y = map(int, sys.stdin.readline().split())

    if x not in x_dict:
        x_dict[x] = [y]
    else:
        x_dict[x].append(y)

# 딕셔너리의 키값들만 오름차순으로 정렬
key_list = sorted(list(x_dict.keys()))

for k in key_list:
    values_list = sorted(list(x_dict[k]))
    for v in values_list:
        print(k, v)


#2
'''
import sys

number = int(sys.stdin.readline())
coordinate = []

for _ in range(number):
    coordinate.append(list(map(int, sys.stdin.readline().split())))

coordinate = sorted(coordinate, key=lambda coordinate: (coordinate[0], coordinate[1]))

for x, y in coordinate:
    print(x, y)
'''