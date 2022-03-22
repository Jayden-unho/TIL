import sys
from collections import deque
sys.stdin = open('input.txt')

def bfs(start):                                             # BFS 탐색
    q = deque([start])  
    visited[start] = 0                                      # 시작 층은 0번 눌러서 도착하므로 0으로 초기화

    while q:
        floor = q.popleft()
        n1, n2 = floor + U, floor - D                       # 올라가는 층, 내려가는 층

        if n1 <= F and visited[n1] == -1:                   # 올라갈 수 있고, 아직 방문한적 없으면
            visited[n1] = visited[floor] + 1                # 방문처리 및 다음 탐색
            q.append(n1)
        if 1 <= n2 and visited[n2] == -1:                   # 내려갈 수 있고, 아직 방문한적 없으면
            visited[n2] = visited[floor] + 1                # 방문처리 및 다음 탐색
            q.append(n2) 


F, S, G, U, D = map(int, sys.stdin.readline().split())      # 건물 최대 높이, 시작 층, 목표 층, 올라가는 층, 내려가는 층
visited = [-1] * (F+1)                                      # 각 층별 방문 여부

bfs(S)                              # 탐색 시작

if visited[G] == -1:                # 목표 층에 도달 못하면 계단 이용 출력
    print('use the stairs') 
else:                               # 목표에 도달 가능하면 누르는 버튼의 최소 횟수 출력
    print(visited[G])