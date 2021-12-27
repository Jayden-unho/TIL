import sys
sys.stdin = open('input.txt')


def DFS(y, x):          
    cheese_boundary = set()                     # 치즈 가장자리
    stack = [(y, x)]                            # DFS 탐색 위한 초기 설정

    while stack:
        node = stack.pop()
        if not visited[node[0]][node[1]]:       # 현재 위치에 치즈가 있는지 확인 안했던 경우
            visited[node[0]][node[1]] = 1       # 확인 체크
            for k in range(4):                  # 상하좌우 확인
                r = node[0] + dr[k]
                c = node[1] + dc[k]
                
                if 0 <= r < N and 0 <= c < M and not visited[r][c]:     # 범위 내이고, 아직 방문하지 않았으면
                    if not board[r][c]:                                 # 치즈가 없는곳이면 다음 DFS 탐색 위해 스택에 좌표 추가
                        stack.append((r, c))
                    elif board[r][c]:                                   # 치즈가 있는곳이면 가장자리이므로 가장자리 리스트에 추가
                        cheese_boundary.add((r, c))

    return cheese_boundary      # 치즈 가장자리 리스트 반환


dr = [-1, 0, 1, 0]              # 델타 탐색
dc = [0, 1, 0, -1]

N, M = map(int, sys.stdin.readline().split())                               # 행의 개수, 열의 개수
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]    # 치즈 상태들 2차원 배열

hour = 0                                            # 흐른 시간
visited = [[0] * M for _ in range(N)]               # 치즈가 있는지 없는지 확인 여부 (방문 변수)
melt_cheese = DFS(0, 0)                             # 녹는 치즈들 명단

while melt_cheese:                                  # 녹는 치즈가 있으면
    remain_cheese = len(melt_cheese)                # 마지막 1시간 전에 남아 있는 치즈를 구하기 위함

    for coor in melt_cheese:                        # 현재 녹는 치즈의 좌표 반복    
        board[coor[0]][coor[1]] = 0                 # 치즈를 녹은걸로 변경

    tmp = []                                        # 임시 저장 리스트 변수
    for i in range(len(melt_cheese)):               # 녹은 치즈들 좌표값을 임시 변수에 저장
        tmp.append(melt_cheese.pop())
    melt_cheese.clear()                             # 다음 시간에 녹는 치즈 명단 비우기
    
    for e in tmp:                                   # 현재 시간에 녹은 치즈들 좌표값 DFS 탐색
        melt_cheese.update(DFS(e[0], e[1]))

    hour += 1                                       # 시간 증가

print(hour)                     # 흐른 시간
print(remain_cheese)            # 마지막 1시간 전 남아있는 치즈의 양