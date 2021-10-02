"""
브루트포스 / 백트랙킹
"""



import os
import sys
import time
from pprint import pprint
sys.stdin = open('input.txt')


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


""" 3 """
def connect_line(y, x, k, num):                 # core 에서 배열 경계까지 라인 추가 / y 좌표, x 좌표, 방향 , 채우는 숫자
    global cnt_line, cnt_core

    # os.system('clear')
    # print('\n')
    # for r in range(N):
    #     for c in range(N):
    #         if processor[r][c] == 0:
    #             print('\033[30m \033[42m', processor[r][c], end=' ')
    #         elif r == pivot[0] and c == pivot[1]:
    #             print('\033[37m \033[40m', processor[r][c], end=' ')
    #         elif processor[r][c] == 1:
    #             print('\033[30m \033[43m', processor[r][c], end=' ')
    #         else:
    #             print('\033[30m \033[45m', processor[r][c], end=' ')
            
                
    #     print()
    # time.sleep(0.5)

    y = y + dr[k]
    x = x + dc[k]

    if y < 0 or x < 0 or y >= N or x >= N:      # 배열 끝까지 도달하면
        cnt_core += 1                        # 연결된 코어의 갯수 증가
        return True                             # 연결되었으므로 True

    elif not processor[y][x]:                   # 좌표 값이 0일때
        processor[y][x] = num
        cnt_line += 1
        result = connect_line(y, x, k, num)     # 좌표 진행 및 코어 연결 여부 결과 저장

        if not result:                          # 끝까지 연결되지 못하면
            processor[y][x] = 0                 # 배열 값들 원래대로 돌려놓음
            cnt_line -= 1

    else:                                       # 좌표 값이 1 또는 다른 전선일때
        return False                            # 연결되지 못하였으므로 False
    return result                               # 코어 연결 여부 반환


""" 4 """
def restore_line(y, x, k, num):                 # 이전 단계로 복원 / 위와 동일
    global cnt_line, cnt_core
    y = y + dr[k]
    x = x + dc[k]

    if y < 0 or x < 0 or y >= N or x >= N:      # 배열 끝까지 전선을 모두 복구 했으면
        cnt_core -= 1                        # 연결된 코어 갯수 감소

    elif processor[y][x] == num:                # 좌표 값이 현재 core에 연결된 전선이면
        cnt_line -= 1                        # 전선 갯수 감소
        processor[y][x] = 0                     # 전선 삭제 (복구)
        restore_line(y, x, k, num)              # 다음 좌표 진행


""" 2 """
def search(idx):            # 경우의 수 탐색
    global answer, max_core, cnt_line, cnt_core # , case, pivot 

    if cnt_core + (M - idx) < max_core:
        
        # print(f'\033[30m\033[101m\n!!!!! 백트래킹 !!!!!')
        # print(f'- 가장 많이 연결된 코어 갯수 : {max_core}')
        # print(f'- 현재 연결된 코어 갯수 : {cnt_core}')
        # print(f'- 남은 프로세서 갯수 : {M-idx}')
        # time.sleep(3)

        return
    elif idx == M:                              # 모든 core 설치했을때
        if max_core != cnt_core:                # 최고 코어 갱신하게 되면
            answer = N * N                      # 이전 코어에서 연결한 최소 전선 갯수 초기화
        max_core = cnt_core

        if answer > cnt_line:                # 현재 경우에 전선의 갯수가 더 적으면
            answer = cnt_line                # 정답에 저장

        # case += 1        
        # print(f'\n------ CASE {case} END ------')
        # print(f'- 지금까지 가장 많이 연결된 코어 갯수 : {max_core}\n')
        # print(f'- 현재 연결된 코어 갯수 : {cnt_core}')
        
        # print(f'- 지금까지 가장 적은 전선의 갯수 : {answer}')
        # print(f'- 현재 전선의 갯수 : {cnt_line}')

        # time.sleep(3)
        
        return
            

    for k in range(4):      # 위, 오른쪽, 아래, 왼쪽 순으로 방향 진행
        
        # pivot = (core_li[idx][0], core_li[idx][1])

        connect_line(core_li[idx][0], core_li[idx][1], k, idx+2)        # 현재 core 전선 연결
        search(idx+1)                                                   # 다음 core 탐색
        restore_line(core_li[idx][0], core_li[idx][1], k, idx+2)        # 앞에 진행한 core 전선 삭제


""" 1 """
T = int(input())

for tc in range(1, T+1):
    N = int(input())                                                    # 프로세서 크기
    processor = [list(map(int, input().split())) for _ in range(N)]       # 프로세서 정보
    answer = N * N                                                      # 전선의 갯수 (모든 공간에 전선이 있는 경우)

    # case = 0
    
    core_li = []                                                        # core 의 좌표값들
    max_core = 0                                                        # 코어 최대 연결 갯수
    cnt_line = 0                                                        # 전선의 갯수
    cnt_core = 0                                                        # 연결된 코어의 갯수

    for i in range(1, N-1):                                             # 테두리에 있는 코어는 필요없음
        for j in range(1, N-1):
            if processor[i][j]:
                core_li.append((i, j))                                  # core 좌표값 리스트에 추가

    M = len(core_li)
    search(0)                                                           # 탐색 / 시작 인덱스, 코어의 갯수

    print('#{} {}'.format(tc, answer))                                  # 가장 많은 Core 를 연결했을때 최소 전선의 갯수 출력