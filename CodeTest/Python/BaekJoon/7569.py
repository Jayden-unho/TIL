'''
3차원 배열 -> 2차원 배열로 만들어서 진행
중간에 헷갈려서 다시 처음부터...
'''

import sys
from collections import deque



def bfs():
    dr = [-1, 1, 0, 0, 0, 0]        # 윗 상자/ 아래 상자
    dc = [0, 0, -M, M, -1, 1]       # 상 / 하 / 좌 / 우
    
    q = deque()
    q.extend(start)

    while q:
        node = q.popleft()
        visited[node[0]][node[1]] += 1

        for k in range(6):
            if node[1] % M == 0 and k == 4:
                continue
            elif node[1] % M == M-1 and k == 5:
                continue
            
            y = node[0] + dr[k]
            x = node[1] + dc[k]
            
            if 0 <= x < M*N and 0 <= y < H and box[y][x] == 0:
                box[y][x] = 1
                visited[y][x] = visited[node[0]][node[1]]
                q.append((y, x))



def answer_search():
    tmp_max = 0

    for i in range(H):
        for j in range(M*N):
            if box[i][j] == 0:
                return -1
            elif visited[i][j] > tmp_max:
                tmp_max = visited[i][j]

    if tmp_max == 0:
        return tmp_max
    return tmp_max-1




M, N, H = map(int, sys.stdin.readline().split())    # 가로 세로 높이


box = []                                                    # 토마토가 담길 박스
for _ in range(H):                                          # 1차원 배열은 높이
    tmp = []                                                # 2차원 배열은 가로 * 세로 / 가로의 배수는 다음 세로줄 의미
    for _ in range(N):
        tmp += list(map(int, sys.stdin.readline().split()))
    box.append(tmp)


start = []                                                  # 익은 토마토가 있는 좌표값을 찾아냄
for i in range(H):
    for j in range(N*M):
        if box[i][j] == 1:
            start.append((i, j))

visited = [[0]*M*N for _ in range(H)]
bfs()

answer = answer_search()
print(answer)


# '''
# 3차원 배열 -> 2차원 배열로 만들어서 진행
# 최소 기간이 필요하므로 DFS탐색
# '''

# import sys
# from collections import deque


# def delta_search():
#     df = [0, 0, 0, 0, -1, 1]        # 위 / 오른쪽 / 아래 / 왼쪽 / 아랫층 / 윗층
#     di = [(-1*N*M), 1, (N*M), -1, 0, 0]

#     for f in range(H):              # Box floor
#         for i in range(N*M):        # Box row & column
#             if box[f][i] != -1:
#                 for k in range(6):
#                     y = f + df[k]
#                     x = i + di[k]

#                     if 0 <= y < H and 0 <= x < M*N and box[y][x] == 0:
#                         linked[(f, i)] = linked.get((f, i), []) + [(y, x)]


# def dfs():
#     q = deque(start)

#     while q:
#         node = q.popleft()
#         for e in linked.get(node, []):
#             if box[e[0]][e[1]] == 0:
#                 q.append(e)
#                 box[e[0]][e[1]] = box[node[0]][node[1]] + 1


# M, N, H = map(int, sys.stdin.readline().split())
# box = []
# linked = {}


# for i in range(H):                                              # 3차원 정보가 담긴 2차원 배열
#     box.append([])
#     for _ in range(N):
#         box[i].extend(list(map(int, sys.stdin.readline().split())))

# start = []
# for a in range(H):
#     for b in range(M*N):
#         if box[a][b] == 1:
#             start.append((a, b))

# delta_search()
# dfs()
# print(box)
# answer = 0
# for i in range(H):
#     tmp = max(box[i])
#     if box[i].count(0):
#         print(-1)
#         break

#     if answer < tmp:
#         answer = tmp
# else:
#     print(answer-1)