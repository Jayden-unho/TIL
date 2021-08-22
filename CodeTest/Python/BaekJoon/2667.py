'''
1. 델타 탐색으로 상하좌우 1인(연결된) 목록을 탐색한다.
2. dfs를 이용하여 한 구역에 연결된게 몇개인지 카운트한다.

놓친 반례
- 해당 좌표 상화좌우는 0인데 본인만 1인 경우 linked 변수에 포함시키지 못하였다.
'''

import sys



def delta_search():                                                         # 델타탐색
    dr = [-1, 0, 1, 0]                                                      # 상하좌우 탐색
    dc = [0, 1, 0, -1]

    for i in range(n):
        for j in range(n):
            if board[i][j] == '1':                                          # 현좌표가 1일때
                linked[(i, j)] = [(i, j)]                                   # 현재 좌표도 연결리스트에 본인 추가
                for k in range(4):                                          
                    y = i + dr[k]
                    x = j + dc[k]

                    if 0 <= x < n and 0 <= y < n and board[y][x] == '1':    # 상하좌우가 인덱스 범위 내이고, 값이 1일때만 linked 리스트에 추가
                        linked[(i, j)] = linked.get((i, j)) + [(y, x)]

def dfs(start):                                                             # dfs
    stack = [start]
    cnt = 0                                                                 # 해당 단지에 집이 몇개인지 확인하기 위해

    while stack:
        node = stack.pop()
        if not visited[node[0]][node[1]]:                                   # 방문한적이 없으면
            cnt += 1
            visited[node[0]][node[1]] = True
            
            for e in linked.get(node):                                      # 다음 연결된곳이 방문된적이 없으면 스택에 추가
                if not visited[e[0]][e[1]]:
                    stack.append(e)
                    
            linked.pop(node)                                                # 연결 확인한 곳은 리스트에서 삭제

    return cnt



n = int(sys.stdin.readline())
board = [sys.stdin.readline().strip() for _ in range(n)]
answer = []

linked = {}
visited = [[False]*n for _ in range(n)]

delta_search()
while linked:                                                               # 연결된 리스트가 남아잇으면 계속해서 다음 단지 탐색
    answer.append(dfs(list(linked.keys())[0]))


answer.sort()       # 출력
print(len(answer))
for e in answer:
    print(e)