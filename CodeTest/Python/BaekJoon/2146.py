import sys
from collections import deque
sys.stdin = open('input.txt')

dr = [-1, 0, 1, 0]                                  # 위 오른쪽 아래 왼쪽
dc = [0, 1, 0, -1]

def numbering(y, x, num):                           # 섬마다 숫자를 매김
    q = deque([(y, x)])                 
    board[y][x] = num                               # 현재 위치부터 섬 번호를 매김

    coors = set()                                   # 해당 섬의 경계의 좌표들을 저장할 변수
    while q:
        y, x = q.popleft()
        for k in range(4):
            r = y + dr[k]
            c = x + dc[k]

            if 0 <= r < N and 0 <= c < N:
                if board[r][c] == 1:                # 옆의 땅을 탐색해서 같은 번호를 매김
                    board[r][c] = num
                    q.append((r, c))
                elif not board[r][c]:               # 주변에 바다가 있으면, 경계이므로
                    coors.add((y, x))

    coordinates.append(coors)                       # 섬들 경계선 좌표를 모아두는 변수에
                                                    # 해당 섬의 경계 좌표를 저장

def bridge_search():                                        # 다리 길이 탐색
    global answer

    for i in range(len(coordinates)):                       # 섬 하나 선택
        for j in range(i+1, len(coordinates)):              # 다른 섬 하나 선택
            for y1, x1 in coordinates[i]:                   # 각 섬들의 경계좌표끼리
                for y2, x2 in coordinates[j]:               # 거리를 구해줌
                    dist = abs(y1-y2) + abs(x1-x2) - 1
                    answer = min(answer, dist)              # 제일 작은 길이만 구함

N = int(sys.stdin.readline())                                               # 보드판의 크기
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]    # 보드판 정보
coordinates = []                        # 섬들 경계선 좌표들
answer = 1e10                           # 정답 초기화

num = 2                                 # 초기 섬 번호
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:            # 육지이면
            numbering(i, j, num)        # 섬 번호 매기기 시작
            num += 1

bridge_search()                         # 다리 건설 탐색

print(answer)