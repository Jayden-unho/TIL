import sys
from pprint import pprint
sys.stdin = open('input.txt')


def dfs(y, x, room_num):
    global room_cnt

    room_cnt += 1
    for k in range(4):
        if not board[y][x] & (1 << k):              # 벽이 뚫려있는 위치 찾아냄
            r = y + dr[k]
            c = x + dc[k]

            if 0 <= r < M and 0 <= c < N and not room[r][c]:    # 다음곳 방문 안했다면
                room[r][c] = room_num                           # 방문체크 후 재귀
                dfs(r, c, room_num)


dr = [0, -1, 0, 1]      # 문제에서 제시로 왼쪽 / 위 / 오른쪽 / 밑
dc = [-1, 0, 1, 0]

N, M = map(int, sys.stdin.readline().split())                               # 가로 / 세로
board = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]    # 성벽 정보
room = [[0]*N for _ in range(M)]                                            # (방문체크) 방의 정보
room_info = {}                                                              # 각 방별로 공간의 크기 담김
room_num = 1                                                                # 방의 갯수 카운트 (방 번호)
room_max = 0                                                                # 방의 크기가 제일 큰 경우 개수
answer = 0                                                                  # 벽을 하나 뚫어서 방이 제일 큰 경우 방의 개수

for i in range(M):
    for j in range(N):
        room_cnt = 0                                                        # 방의 개수 카운트
        if not room[i][j]:                                                  # 방 체크 안했으면 (방문 안했으면)
            room[i][j] = room_num                                           # 방문 체크
            dfs(i, j, room_num)                                             # 같은 방 탐색
            room_info[room_num] = room_info.get(room_num, 0) + room_cnt     # 방의 개수 저장
            if room_max < room_cnt:                                         # 해당 방이 최대 개수인지 판별
                room_max = room_cnt
            room_num += 1                                                   # 다음 방
            # print(f'----- room -----')
            # pprint(room)
            # print(f'LOG --- room_info : {room_info}')

for i in range(M):                  # 벽 하나 뚫었을때 방의 최대 개수 구하기 위함
    for j in range(N):
        for k in range(2, 4):       # 오른쪽 밑에만 보면 됨
            r = i + dr[k]
            c = j + dc[k]

            if 0 <= r < M and 0 <= c < N and room[i][j] != room[r][c]:      # 범위 안이고 서로 다른 방이면
                tmp = room_info[room[i][j]] + room_info[room[r][c]]         # 서로 다른 방 개수 합치기
                if answer < tmp:
                    answer = tmp

print(room_num - 1)
print(room_max)
print(answer)