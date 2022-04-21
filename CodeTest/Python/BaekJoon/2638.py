import sys
sys.stdin = open('input.txt')

def set_air(melted = []):                                           # 공기의 영역을 새로 구하는 함수
    stack = melted or [(0, 0)]                                      # 녹는 치즈가 있으면 초기값으로 설정 없다면 0,0 을 초기값으로 설정

    while stack:                                                    
        node = stack.pop()
        if not air[node[0]][node[1]]:                               # 탐색하지 않은 영역이면
            air[node[0]][node[1]] = 1                               # 공기로 표시

            for k in range(4):                                      # 이어서 탐색
                r = node[0] + dr[k]
                c = node[1] + dc[k]

                if 0 <= r < N and 0 <= c < M and not board[r][c]:
                    stack.append((r, c))

dr = [-1, 0, 1, 0]                                                          # 위 오른쪽 아래 왼쪽
dc = [0, 1, 0, -1]

N, M = map(int, sys.stdin.readline().split())                               # 세로, 가로
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]    # 모눈종이

cheeze = set()                              # 치즈 좌표들 모음
air = [[0] * M for _ in range(N)]           # 공기를 표시한 2차원 배열

set_air()                                   # 초기 공기의 영역을 구함

for i in range(N):                          # 치즈의 좌표들을 구함
    for j in range(M):
        if board[i][j] == 1:
            cheeze.add((i, j))

hour = 0
while cheeze:                               # 치즈가 남아있으면 반복
    hour += 1
    melted = []                             # 녹은 치즈들의 좌표

    for c in cheeze:                        # 치즈 좌표 하나씩 탐색
        cnt = 0

        for k in range(4):                  # 상하좌우 좌표를 새로 구함
            y = c[0] + dr[k]
            x = c[1] + dc[k]

            if air[y][x]:                   # 만약 공기와 맞닿아있으면
                cnt += 1                    # 개수 카운트
        
        if cnt >= 2:                        # 두칸 이상 공기와 맞닿아 있다면,
            melted.append((c[0], c[1]))     # 녹을 치즈 좌표 리스트에 추가

    for item in melted:                     # 현재 치즈에서 녹을 치즈들을 모두 제거
        cheeze.remove(item)
    
    set_air(melted)                         # 녹은 치즈들을 기준으로 하여 공기의 영역 새로 구함

print(hour)