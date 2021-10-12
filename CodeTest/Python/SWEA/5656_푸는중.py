import os
import time
import sys
from itertools import combinations_with_replacement
sys.stdin = open('input.txt')


def dfs(y, x, k, remain):       # coordinate / direction / remain_move
    global tmp_cnt

    if remain <= 0:
        return
    if elements == (2,2,6):
        for q in range(H):
            for w in range(W):
                print(tmp_board[q][w], end=' ')
            print()
        print(f'떨어지는 공위치 : {e}, 남은 이동 : {remain}')
        print(f'tc_answer : {max_broken}, tmp_cnt : {tmp_cnt}')
        time.sleep(1)

        os.system('clear')

    r = y + dr[k]
    c = x + dc[k]

    if 0 <= r < H and 0 <= c < W:
        if tmp_board[r][c]:
            tmp_cnt += 1
            # remain = tmp_board[r][c]-1
            
            if tmp_board[r][c] != 1:
                for a in range(4):
                    if (k+2)%4 != a:
                        dfs(r, c, a, remain)
            tmp_board[r][c] = 0
            
            for a in range(c, 0, -1):
                if tmp_board[r][a-1] == 0:
                    break
                tmp_board[r][a], tmp_board[r][a-1] = tmp_board[r][a-1], tmp_board[r][a]


        dfs(r, c, k, remain-1)



dr = [-1, 0, 1, 0]      # 상 / 우 / 하 / 좌
dc = [0, 1, 0, -1]

T = int(input())
answer = []

for tc in range(1, T+1):
    N, W, H = map(int, input().split())                             # 공 떨어뜨리는 횟수 / 너비 / 높이
    board = [list(map(int, input().split())) for _ in range(H)]     # 보드판 정보 (안의 숫자만큼 십자가 모양으로 블록이 터짐)
    tc_answer = 0
    max_broken = 0

    for i in range(H):
        for j in range(W):
            if board[i][j]:
                tc_answer += 1

    for elements in set(combinations_with_replacement(range(W), N)):
        tmp_board = list(map(list, zip(*board)))
        tmp_cnt = 0
        if elements == (2,2,6):
            for e in elements:
                print(tmp_board)
                print(e)
                for j in range(H):
                    if tmp_board[e][j]:
                        remain = tmp_board[e][j]-1
                        tmp_cnt += 1
                        tmp_board[e][j] = 0
                        for k in range(3):
                            dfs(e, j, k, remain)
                        break
        
        if max_broken < tmp_cnt:
            max_broken = tmp_cnt

    tc_answer -= max_broken

    answer.append('#{} {}'.format(tc, tc_answer))

print(*answer, sep='\n')