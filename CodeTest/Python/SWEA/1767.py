"""
dfs 통한 브루트포스
모든 코어를 연결했을 경우부터 내려가야함
"""

import sys
from pprint import pprint
sys.stdin = open('input.txt')


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def connect_line(start, k, num):
    global connect_chip, line

    result = False

    y = start[0] + dr[k]
    x = start[1] + dc[k]

    if 0 <= y < N and 0 <= x < N and not chip[y][x]:
        chip[y][x] = num
        result = connect_line((y, x), k, num)
        line += 1
        if not result:
            chip[y][x] = 0
            line -= 1

    elif y == -1 or x == -1 or y == N or x == N:
        connect_chip += 1
        return True
    elif chip[y][x] == 1 or chip[y][x] == num:
        return False    
    return result


def restore(start, k, num):
    global connect_chip, line

    y = start[0] + dr[k]
    x = start[1] + dc[k]

    if 0 <= y < N and 0 <= x < N and chip[y][x] == num:
        line -= 1
        chip[y][x] = 0
        restore((y, x), k, num)
    elif y == -1 or x == -1 or y == N or x == N:
        connect_chip -= 1
    elif not chip[y][x]:
        return


def solution(idx, n):
    global connect_chip, answer, min_line

    if idx == n:
        if answer <= connect_chip:
            if answer != connect_chip:
                min_line = N * N
            answer = connect_chip
            # print('------', answer, connect_chip)


            if line < min_line:
                min_line = line
        return
    elif connect_chip + (n - idx) < answer:
        return

    for k in range(4):
        connect_line(need_chip[idx], k, idx+2)
        solution(idx+1, n)
        restore(need_chip[idx], k, idx+2)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    chip = [list(map(int, input().split())) for _ in range(N)]
    
    need_chip = []
    connect_chip = 0
    answer = 0
    min_line = N * N
    line = 0

    for i in range(1, N-1):
        for j in range(1, N-1):
            if chip[i][j]:
                need_chip.append((i, j))
    # print(f'LOG --- NEED_CHIP : {need_chip}')
    
    solution(0, len(need_chip))

    print('#{} {}'.format(tc, min_line))