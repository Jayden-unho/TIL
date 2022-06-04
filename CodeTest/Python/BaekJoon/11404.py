import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())                                               # 노드의 개수
M = int(sys.stdin.readline())                                               # 간선의 개수
distance = [[1e10] * N for _ in range(N)]                                   # 노드간 최소 거리

for _ in range(M):                                                          # 간선들 정보
    start, end, weight = map(int, sys.stdin.readline().split())             # 노드간 거리 최소값 갱신
    distance[start-1][end-1] = min(distance[start-1][end-1], weight)

for k in range(N):
    distance[k][k] = 0                                                      # 본인 노드로 가는 거리는 0으로 할당
    for i in range(N):
        for j in range(N):
            distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])       # 중간에 다른 노드를 거쳐서 가는 경우와, 바로 가는 경우 중 더 작은 값을 저장

for i in range(N):
    for j in range(N):
        if distance[i][j] == 1e10:          # 해당 노드로 이동 할 수 없는 경우 0으로 할당
            distance[i][j] = 0
    print(*distance[i])                     # 출력

# import sys
# import heapq
# sys.stdin = open('input.txt')

# def solution(start):
#     h = [(0, start)]
#     distance = [-1] * (N+1)

#     while h:
#         node = heapq.heappop(h)
#         if distance[node[1]] == -1:
#             distance[node[1]] = node[0]
#             for next in linked[node[1]]:
#                 heapq.heappush(h, (next[0]+node[0], next[1]))

#     return distance[1:]

# N = int(sys.stdin.readline())
# M = int(sys.stdin.readline())
# linked = [[] for _ in range(N+1)]

# for _ in range(M):
#     start, end, weight = map(int, sys.stdin.readline().split())
#     linked[start].append((weight, end))

# for i in range(1, N+1):
#     print(*solution(i))