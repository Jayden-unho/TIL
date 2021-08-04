import sys
from pprint import pprint



def dfs_func(y, x):
    move_x = [1, 0, -1, 0]
    move_y = [0, 1, 0, -1]
    
    dfs_stack = [[x, y]]
    visit_stack = []
    
    while dfs_stack:
        coordinate = dfs_stack.pop()
        if coordinate not in visit_stack:
            visit_stack.append(coordinate)
            for idx in range(4):
                tmp_x = coordinate[0] + move_x[idx]
                tmp_y = coordinate[1] + move_y[idx]
                if 0 <= tmp_x and tmp_x < width and 0 <= tmp_y and tmp_y < height and land[tmp_y][tmp_x] == 1:
                    land[tmp_y][tmp_x] = 0
                    dfs_stack.append([tmp_x, tmp_y])




test_case = int(sys.stdin.readline())


for _ in range(test_case):
    width, height, number = map(int, sys.stdin.readline().split())
    answer = 0  # 필요한 최소 배추흰지렁이 마리수


    # 땅을 만들고 배추가 심어진곳 1로 만듦
    land = [[0 for _ in range(width)] for _ in range(height)]

    for _ in range(number):
        x, y = map(int, sys.stdin.readline().split())
        land[y][x] = 1


    for y in range(height):
        for x in range(width):
            if land[y][x] == 1:
                answer += 1
                land[y][x] = 0
                dfs_func(y, x)

    print(answer)