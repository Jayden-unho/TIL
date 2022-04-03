import sys
from pprint import pprint
sys.stdin = open('input.txt')

dr = [-1, -1, 0, 1, 1, 1, 0, -1]        # 위 왼쪽위 왼쪽 왼쪽아래 아래 오른쪽아래 오른쪽 오른쪽위
dc = [0, -1, -1, -1, 0, 1, 1, 1]

def solution(y, x, direction, ans):
    global answer
    print('----- start ----')
    print(y, x, direction, ans)
    
    for k in sorted(fish_coordinates.keys()):
        fy, fx, fd = fish_coordinates[k]
        for idx in range(8):
            new_fd = (fd+idx) % 8
            r = fy + dr[new_fd]
            c = fx + dc[new_fd]

            if 0 <= r < 4 and 0 <= c < 4 and fish_coordinates.get(sea[(r, c)], True) and (r, c) != (y, x):
                fish_coordinates[k] = (r, c, new_fd)

                if fish_coordinates.get(sea[(r, c)], False):
                    fish_coordinates[sea[(r, c)]] = (fy, fx, fish_coordinates[sea[(r, c)]][2])
                    sea[(fy, fx)], sea[(r, c)] = sea[(r, c)], sea[(fy, fx)]
                else:
                    sea[(r, c)] = k
                    sea[(fy, fx)] = 17
                
                break
    
    for i in range(1, 4):
        r = y + dr[direction] * i
        c = x + dc[direction] * i
        print(f'r: {r}, c: {c}')
        if 0 <= r < 4 and 0 <= c < 4 and fish_coordinates.get(sea[(r, c)], False):

            print(fish_coordinates)
            print(f'y: {y} | x: {x} | r: {r} | c: {c} | fish_num: {sea[(r, c)]}')
            print(ans, sea[(r, c)])

            pre_y, pre_x, pre_d = fish_coordinates.pop(sea[(r, c)])
            print(f'answer : {answer} | ans+sea[(r, c)]: {ans+sea[(r, c)]}')

            answer = max(answer, ans+sea[(r, c)])
            solution(r, c, pre_d, ans+sea[(r, c)])
            fish_coordinates[sea[(r, c)]] = (pre_y, pre_x, pre_d)


sea = {(i, j): '' for j in range(4) for i in range(4)}              # 좌표별 물고기 번호
fish_coordinates = {k:'' for k in range(1, 17)}                     # 물고기 번호별 현재 위치, 진행 방향

for i in range(4):
    info = list(map(int, sys.stdin.readline().split()))
    for j in range(4):
        sea[(i, j)] = info[j*2]
        fish_coordinates[info[j*2]] = (i, j, info[j*2+1]-1)

start_fish = sea[(0, 0)]
y, x, d = fish_coordinates.pop(start_fish)
answer = start_fish
solution(0, 0, d, start_fish)

print(answer)