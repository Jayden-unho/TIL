import sys
sys.stdin = open('input.txt')

def solution():
    new_move = set()                    # 다음에 움직여야 할 고슴도치, 물 좌표들
    new_water = set()                   

    for y, x in move:                   # 고슴도치가 이동하는 좌표
        for k in range(4):              # 인접한 다음 좌표
            r = y + dr[k]
            c = x + dc[k]

            if 0 <= r < R and 0 <= c < C and not visited[r][c]:     # 고슴도치가 이동 가능한 곳이라면
                visited[r][c] = visited[y][x] + 1                   # 이동 거리 기록
                new_move.add((r, c))                                # 다음번에 움직일 고슴도치 좌표 추가
    
    for y, x in water:                      # 물이 이동하는 좌표
        for k in range(4):                  # 인접한 다음 좌표
            r = y + dr[k]
            c = x + dc[k]

            if 0 <= r < R and 0 <= c < C and 0 <= visited[r][c] and land[r][c] != 'D':  # 물이 이동 가능한 곳이라면
                visited[r][c] = -1          # 물이 이동됬다면 음수로 기록
                new_water.add((r, c))       # 다음번에 움직일 물 좌표 추가
    
    return new_move, new_water              # 다음번에 움직일 좌표들 반환


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

R, C = map(int, sys.stdin.readline().split())                   # 행, 열
land = [list(sys.stdin.readline().strip()) for _ in range(R)]   # 땅의 정보
visited = [[0] * C for _ in range(R)]                           # 위치별 이동 거리 또는 물 침범 유무
water = set()                               # 이동해야 할 물의 좌표들
move = set()                                # 이동해야 할 고슴도치의 위치

for i in range(R):
    for j in range(C):
        if land[i][j] == 'D':           # 도착지 정보 기록
            end = (i, j)
        elif land[i][j] == 'S':         # 출발지
            move.add((i, j))            # 출발 위치의 값을 1로 설정
            visited[i][j] = 1 
        elif land[i][j] == '*':         # 물인 경우
            water.add((i, j))           # 다음번에 이동해야 할 물의 좌표 추가
            visited[i][j] = -1          # 방문 리스트에 음수를 기록하여 고슴도치가 이동하지 못하도록 설정
        elif land[i][j] == 'X':         # 벽인 경우
            visited[i][j] = -1          # 물과 고슴도치가 이동하지 못하도록 음수 기록

while move:                             # 고슴도치가 이동할 좌표가 남아있다면
    if visited[end[0]][end[1]]:         # 목적지 도착했으면 반복문 종료
        break
    move, water = solution()            # 다음에 이동해야 할 고슴도치의 좌표들과 물의 좌표들
    move = move.difference(water)       # 고슴도치가 있었으나, 물이 들어오면서 이동 불가능한 고슴도치 좌표 제거

answer = visited[end[0]][end[1]] - 1    # 목적지에 이동하기 위한 최소 시간
if answer > 0:
    print(answer)
else:
    print('KAKTUS')