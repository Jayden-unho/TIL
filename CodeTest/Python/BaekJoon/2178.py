'''
1. 상하좌우 델타탐색을 이용하여 해당 좌표에서 움직일 수 있는 칸을 저장한다.
2. BFS 이용하여 최소 이동 거리를 구한다.

로직과 정답이 계속 맞았으나 제출시 틀렸다고 나옴
-> 공간복잡도 생각이 필요함
-> 연결된 좌표들 리스트에 불필요한 데이터 줄임, 큐에 쌓이는 데이터를 줄임
'''

import sys
from collections import deque


def delta_func():                                                                       # 델타 탐색
    dr = [-1, 0, 1, 0]                                                                  # 위, 오른쪽, 아래, 왼쪽
    dc = [0, 1, 0, -1]

    for r in range(n):                                                                  # n번 만큼
        for c in range(m):                                                              # m번 만큼
            if maze[r][c] == '1':                                                       # 현재 위치가 1인 경우에만 실행
                for a in range(4):                                                      # 4개 방향
                    y = r + dr[a]                                                       # 현재 좌표의 상하좌우 좌표 저장
                    x = c + dc[a]

                    if 0 <= x < m and 0 <= y < n and maze[y][x] == '1':                 # 상하좌우 좌표가 인덱스 범위 안이고, 주변 좌표 값이 1일때
                        linked_list[(r, c)] = linked_list.get((r, c), []) + [(y, x)]    # 현위치 키값이 없으면 빈 리스트를 만들고, 현재 좌표값 추가



def bfs_func(start):                                # 최소 거리를 구해야하므로 너비 우선 탐색
    queue = deque([start])                          # 큐에 시작 좌표를 넣음
    last = start                                    # 현재 레벨의 마지막 노드
    result = 2                                      # 출발과 도착할때도 숫자를 카운트 해야하므로

    while queue:                                    # 큐에 값이 남아있으면, 더 이상 진행이 불가능할때
        node = queue.popleft()                      # 큐의 왼쪽에서 값을 꺼냄
        if not visited[node[0]][node[1]]:           # 해당 좌표 방문한적이 없으면
            visited[node[0]][node[1]] = True        # 해당 좌표 방문으로 값 변경
            
            for e in linked_list.get(node):
                if not visited[e[0]][e[1]]:
                    queue.append(e)                 # 현재 위치에서 갈수 있는 길을 큐에 추가

        if (n-1, m-1) in linked_list.get(node):     # 도착 좌표가 있으면
            return result                           # 몇스텝을 왔는지 반환

        if last == node:                            # 현재 레벨의 마지막 노드에 도착하면
            result += 1                             # 단계 + 1
            last = queue[-1]                        # 현재 큐에 있는 맨 뒤의 값을 다음 레벨 마지막 노드로 선택
    
    return '출구로 접근 불가'


n, m = map(int, sys.stdin.readline().split())       # n - row 갯수 / m - col 갯수
maze = [input() for _ in range(n)]                  # row 갯수만큼 입력 받음 / 1차원 배열 각 요소는 row 한줄의 문자열이 담김 ex) ['101111', '101010', '101011', '111011']
linked_list = {}                                    # 현재 좌표에서 다음 좌표로 이동 가능한 경로를 저장하는 딕셔너리 변수
visited = [[False]*m for _ in range(n)]             # 좌표에서 방문했는지 여부를 저장하는 2차원 배열

delta_func()                                        # 현재 좌표에서 다음 이동을 어디로 할 수 있는지 탐색
answer = bfs_func((0, 0))                           # 0,0에서 출발

print(answer)