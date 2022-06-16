import sys
sys.setrecursionlimit(1000000)
sys.stdin = open('input.txt')

dr = [-1, 0, 1, 0]                  # 상 우 하 좌
dc = [0, 1, 0, -1]

def solution(y, x):
    if visited[y][x]:               # 해당 좌표에서 최대로 이동 가능한 경로를 이미 아는 경우
        return visited[y][x]        # 남은 이동 수 반환
    
    visited[y][x] = 1               # 현재 좌표에서 1칸 이동 가능하다고 설정
    for k in range(4):              # 인접 좌표 확인
        r = y + dr[k]
        c = x + dc[k]

        if 0 <= r < N and 0 <= c < N and board[y][x] < board[r][c]:     # 현재 좌표보다 더 많은 대나무가 있으면
            visited[y][x] = max(visited[y][x], solution(r, c) + 1)      # 재귀로 다음 좌표 탐색
    return visited[y][x]                                                

N = int(sys.stdin.readline())                                               # 대나무 숲 크기
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]    # 대나무 숲 정보
visited = [[0] * N for _ in range(N)]                                       # 좌표별 이동 가능한 수
answer = 0

for i in range(N):
    for j in range(N):
        if not visited[i][j]:                       # 현재 좌표에서 이동 가능한 경로 수를 모르는 경우
            answer = max(answer, solution(i, j))    # 탐색하고, 정답과 비교하여 더 큰 값 저장
print(answer)