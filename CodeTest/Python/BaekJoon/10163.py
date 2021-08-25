'''
시간복잡도, 공간복잡도 생각하기
'''

# 69% 에서 실패
import sys

N = int(input())


x, y, p, q = 1100, 1100, 0, 0
paper_list = []

for _ in range(N):
    tmp_x, tmp_y, tmp_width, tmp_height = map(int, sys.stdin.readline().split())
    paper_list.append([tmp_x, tmp_y, tmp_x + tmp_width, tmp_y + tmp_height])

    if tmp_x < x:
        x = tmp_x
    if tmp_y < y:
        y = tmp_y
    if tmp_x + tmp_width > p:
        p = tmp_x + tmp_width
    if tmp_y + tmp_height > q:
        q = tmp_y + tmp_height

board = [[0]*(p-x) for _ in range(q-y)]

remain = (p-x) * (q-y)
stack = []
idx = N
while paper_list and remain > 0:
    e = paper_list.pop()
    cnt = 0
    for i in range(e[1]-y, e[3]-y):
        for j in range(e[0]-x, e[2]-x):
            if not board[i][j]:
                board[i][j] = idx
                cnt += 1
                remain -= 1
    stack.append(cnt)
    idx -= 1

while stack:
    print(stack.pop())









# 틀림
# import sys
# from collections import deque

# N = int(input())


# y, q = 1100, 0
# paper_list = []

# for _ in range(N):
#     tmp_x, tmp_y, tmp_width, tmp_height = map(int, sys.stdin.readline().split())
#     paper_list.append([tmp_x, tmp_y, tmp_x + tmp_width, tmp_y + tmp_height])

#     if tmp_y < y:
#         y = tmp_y
#     if tmp_y + tmp_height > q:
#         q = tmp_y + tmp_height

# board = [deque() for _ in range(q-y)]  # [x, p]

# stack = []
# while paper_list:
#     e = paper_list.pop()
#     cnt = e[2] - e[0]

#     for i in range(e[1]-y, e[3]-y):
#         if not board[i]:
#             board[i].extend([e[0], e[2]])
#         else:
#             for j in range(0, len(board[i]), 2):
#                 if e[2] < board[i][j]:
#                     board[i].extendleft([e[0], e[2]])
#                 elif e[0] > board[i][j+1]:
#                     pass


#         if board[i][0] > e[0]:
#             cnt += board[i][0] - e[0]
#             board[i][0] = e[0]
#         if e[2] > board[i][1]:
#             cnt += e[2] - board[i][1]
#             board[i][1] = e[2]

#     stack.append(cnt)

# while stack:
#     print(stack.pop())    
    


# stack = []
# idx = N
# while paper_list:
#     e = paper_list.pop()
#     cnt = 0
#     for i in range(e[1]-y, e[3]-y):
#         for j in range(e[0]-x, e[2]-x):
#             if not board[i][j]:
#                 board[i][j] = idx
#                 cnt += 1
#     stack.append(cnt)
#     idx -= 1

# while stack:
#     print(stack.pop())



'''
import sys


N = int(input())

paper_list = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


for i in range(N-1, -1, -1):
    area = paper_list[i][2] * paper_list[i][3]
    x1 = paper_list[i][0]
    y1 = paper_list[i][1]
    p1 = paper_list[i][0] + paper_list[i][2]
    q1 = paper_list[i][1] + paper_list[i][3]

    center = [[x1, y1, p1, q1]]
    left_top = [x1, q1]
    right_top = [p1, q1]
    left_bottom = [x1, y1]
    right_bottom = [q1, y1]

    for j in range(N-1, i, -1):
        if paper_list[j][-1] == 0:
            continue

        x2 = paper_list[j][0]
        y2 = paper_list[j][1]
        p2 = paper_list[j][0] + paper_list[j][2]
        q2 = paper_list[j][1] + paper_list[j][3]

        if x1 >= p2 or p1 <= x2 or q1 <= y2 or y1 >= q2:    # 사각형 범위 밖이면
            continue
        elif x1 <= x2 <= p1 and y1 <= y2 <= q1 and x1 <= p2 <= p1 and y1 <= q2 <= q1:
            area -= paper_list[j][-1]
        elif left_top[0] < p2 < p1 and y1 < y2 < left_top[1]:
            area += (left_top[0]-x1) * (q1-left_top[1])
            area -= (p2-x1) * (q1-y2)
            left_top[0] = p2
            left_top[1] = y2
        elif x1 <= x2 <= right_top[0] and y1 <= y2 <=right_top[1]:
            area += (p1-right_top[0]) * (q1-right_top[1])
            area -= (p1-x2) * (q1-y2)
            right_top[0] = x2
            right_top[1] = y2
        elif left_bottom[0] <= p2 <= q1 and left_bottom[1] <= q2 <= q1:
            area += (left_bottom[0]-x1) * (left_bottom[1]-y1)
            area -= (p2-x1) * (q2-y1)
            left_bottom[0] = p2
            left_bottom[1] = q2
        elif x1 <= x2 <= right_bottom[0] and right_bottom[1] <= q2 <= q1:
            area += (p1-right_bottom[0]) * (right_bottom[1]-y1)
            area -= (p1-x2) * (q2-y1)
            right_bottom[0] = x2
            right_bottom[1] = q2
    
    paper_list[i].append(area)

for e in paper_list:
    print(e[-1])
'''