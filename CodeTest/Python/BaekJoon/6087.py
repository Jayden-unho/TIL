import sys
from collections import deque
sys.stdin = open('input.txt')

def solution(start):
    q = deque()
    for k in range(4):                              # 시작 좌표는 4가지 방향으로 시작할 수 있음
        q.append((start[0], start[1], k, 0))        # 좌표, 진행 방향, 거울 사용 개수
    
    while q:
        y, x, d, ans = q.popleft()
        r = y + dr[d]                               # 진행 방향을 통해 다음칸 좌표
        c = x + dc[d]

        # 범위내의 좌표이고, 벽면이 아니며, 거울 사용 횟수가 같거나 적을때만
        if 0 <= r < H and 0 <= c < W and board[r][c] != '*' and visited[r][c] >= ans:
            visited[r][c] = ans                     # 거울 사용 횟수 기록
            for k in [-1, 0, 1]:                    # 진행 방향의 왼쪽, 유지, 오른쪽
                nd = (d+k) % 4                      # 다음 새로운 방향
                if k:                               # 새로운 진행 방향이라면 거울 사용 추가
                    q.append((r, c, nd, ans+1))
                else:                               # 방향 유지라면 거울 사용 안함
                    q.append((r, c, nd, ans))
                
dr = [-1, 0, 1, 0]      # 위 오른쪽 아래 왼쪽
dc = [0, 1, 0, -1]

W, H = map(int ,sys.stdin.readline().split())                       # 열, 행의 개수
board = [list(sys.stdin.readline().strip()) for _ in range(H)]      # 지도의 정보
visited = [[1e10] * W for _ in range(H)]      # 각 좌표 도달 필요 거울 개수, 진행방향

points = []                             # 시작, 도착 좌표

for i in range(H):
    for j in range(W):
        if board[i][j] == 'C':
            points.append((i, j))

solution(points.pop())                  # 탐색

end = points.pop()                      # 도착 좌표
print(visited[end[0]][end[1]])          # 목적지 도착에 필요한 거울의 개수