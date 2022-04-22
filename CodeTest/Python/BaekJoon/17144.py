import sys
sys.stdin = open('input.txt')

R, C, T = map(int, sys.stdin.readline().split())                                # 행, 열, 시간
board = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]        # 초기 입력값
cleaner = []                                                                    # 공기청정기 위치

dr = [-1, 0, 1, 0]                              # 위 오른쪽 아래 왼쪽
dc = [0, 1, 0, -1]

for i in range(R):                              # 공기청정기 위치 찾기
    if board[i][0] == -1:
        cleaner.append((i, 0))

def dust_move(board):                           # 미세먼지 이동 함수
    new_board = [[0] * C for _ in range(R)]     # 미세먼지가 이동한 결과를 담을 새로운 2차원 배열
    
    for i in range(R):
        for j in range(C):
            if (i, j) in cleaner:               # 공기청정기 좌표라면, -1 로 지정
                new_board[i][j] = -1
            elif board[i][j] > 0:               # 미세먼지가 있으면
                amount = board[i][j] // 5       # 이동될 먼지 양
                remain = board[i][j]            # 현재 위치에 남은 먼지 양
                for k in range(4):
                    r = i + dr[k]
                    c = j + dc[k]

                    if 0 <= r < R and 0 <= c < C and board[r][c] != -1:     # 주변 좌표가 정상적이고 공기청정기가 아닐때
                        remain -= amount                                    # 현재 위치 남은 먼지양 줄이기
                        new_board[r][c] += amount                           # 이동한 결과를 담을 배열에 이동된 먼지양 추가
                new_board[i][j] += remain                                   # 현재 좌표의 남은 먼지양 추가

    return new_board

def air_cleaner(y, x, k, direction, dust):                                  # 공기청정기 가동 (현재 좌표, 위쪽 공기청정기 or 아래쪽 공기청정기
                                                                            # 진행방향, 먼지양)
    if y == cleaner[k][0] and x == cleaner[k][1]:                           # 공기청정기로 들어왔으면 종료
        return
    elif not (0 <= y < R and 0 <= x < C):                                   # 범위를 벗어나는 좌표라면 진행 방향 회전
        y -= dr[direction]
        x -= dc[direction]
        direction = (direction - 1) % 4 if not k else (direction + 1) % 4
        y += dr[direction]
        x += dc[direction]
        air_cleaner(y, x, k, direction, dust)
    else:                                                                   # 먼지 한칸씩 이동
        move_dust = board[y][x]
        board[y][x] = dust
        y += dr[direction]
        x += dc[direction]
        air_cleaner(y, x, k, direction, move_dust)

while T > 0:                                                            # 시간이 남았다면 반복
    T -= 1

    board = dust_move(board)                                            # 먼지 이동
    air_cleaner(cleaner[0][0], cleaner[0][1]+1, 0, 1, 0)                # 위쪽 공기청정기 가동
    air_cleaner(cleaner[1][0], cleaner[1][1]+1, 1, 1, 0)                # 아래쪽 공기청정기 가동

answer = 2                      # 공기청정기의 좌표값이 -1 이므로 초기값은 2로 설정
for i in range(R):
    answer += sum(board[i])

print(answer)