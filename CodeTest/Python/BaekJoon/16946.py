import sys
sys.stdin = open('input.txt')


def dfs(y, x):
    stack = [(y, x)]
    wall = set()        # 벽 좌표
    num = 0             # 이어지는 빈 공간의 개수

    while stack:
        y, x = stack.pop()
        if (y, x) not in visited:
            visited.add((y, x))
            num += 1                    # 이어지는 빈 공간 카운트
            for k in range(4):
                r = y + dr[k]
                c = x + dc[k]

                if 0 <= r < N and 0 <= c < M:
                    # 이어진 빈 공간이면 스택에 추가
                    if board[r][c] == '0' and (r, c) not in visited:
                        stack.append((r, c))
                    # 벽을 만난다면, 벽을 리스트에 추가
                    elif board[r][c] == '1':
                        wall.add((r, c)
                                 )
    # 벽이였던 곳은 빈공간의 개수만큼 추가 (10으로 나눈 나머지)
    for y, x in wall:
        answer[y][x] += num % 10


dr = [-1, 0, 1, 0]      # 위 오른쪽 아래 왼쪽
dc = [0, 1, 0, -1]

# 입력 값
N, M = map(int, sys.stdin.readline().split())
board = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(N)]

answer = [[0] * M for _ in range(N)]    # 정답
visited = set()                         # 방문 여부

for i in range(N):
    for j in range(M):
        # 빈 공간이고 탐색하지 않은 좌표는 DFS 탐색
        if board[i][j] == '0' and (i, j) not in visited:
            dfs(i, j)
        # 벽이면, 벽을 부쉈을 때 해당 위치도 카운트이므로 1 추가
        elif board[i][j] == '1':
            answer[i][j] += 1

for i in range(N):                      # 출력
    for j in range(M):
        print(answer[i][j] % 10, end='')
    print()
