import sys
from pprint import pprint



def dfs_func(x, y):
    move_x = [1, 0, -1, 0]
    move_y = [0, 1, 0, -1]

    dfs_stack = [[x, y]]
    visit_stack = []

    while dfs_stack:
        coordinate = dfs_stack.pop()
        if coordinate not in visit_stack:
            visit_stack.append(coordinate)
            for i in range(4):
                x = coordinate[0] + move_x[i]
                y = coordinate[1] + move_y[i]
                if 0 <= x < width and 0 <= y < height and land[y][x] == 1:
                    land[y][x] = 0
                    dfs_stack.append([x,y])





test_case = int(sys.stdin.readline())

for _ in range(test_case):
    width, height, number = map(int, sys.stdin.readline().split())
    land = [[0]*width for _ in range(height)]
    count = 0

    # 배추가 있는 땅을 1로 변경
    for _ in range(number):
        x, y = map(int, sys.stdin.readline().split())
        land[y][x] = 1

    for y in range(height):
        for x in range(width):
            if land[y][x] == 1:
                dfs_func(x, y)
                count += 1
                land[y][x] = 0

    print(count)