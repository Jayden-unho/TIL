import sys
import heapq
sys.stdin = open('input.txt')

def solution(start):
    heap = [(0, start)]
    distance = [-1] * (n+1)                                         # 반환할 최단 거리

    while heap:
        node = heapq.heappop(heap)
        if distance[node[1]] == -1:                                 # 도착하지 않았으면
            distance[node[1]] = node[0]                             # 최단 거리 갱신

            for next in linked[node[1]]:
                heapq.heappush(heap, (next[0]+node[0], next[1]))    # 다음 탐색
    
    return distance


T = int(sys.stdin.readline())

for _ in range(T):
    n, m, t = map(int, sys.stdin.readline().split())        # 교차로, 도로, 목적지 개수
    s, g, h = map(int, sys.stdin.readline().split())        # 출발지, 두개의 노드

    linked = [[] for _ in range(n+1)]                           # 연결 관계
    answers = []                                                # 정답

    for _ in range(m):                                          # 연결 관계 정리
        a, b, d = map(int, sys.stdin.readline().split())
        linked[a].append((d, b))                                # (거리, 도착 노드)
        linked[b].append((d, a))

    targets = {int(sys.stdin.readline()) for _ in range(t)}     # 목적지 노드 목록

    distance_s = solution(s)            # 출발지, g, h 에서 도착 노드까지의 최단 거리
    distance_g = solution(g)
    distance_h = solution(h)

    for target in sorted(targets):      # 출발지->g(h)->h(g)->도착지 의 부분별로 구한 거리가 최단거리인 경우
        if distance_s[g] + distance_g[h] + distance_h[target] == distance_s[target] or\
            distance_s[h] + distance_h[g] + distance_g[target] == distance_s[target]:
            answers.append(target)
    
    print(*answers)


# def solution(start, targets):
#     heap = [(0, start, set())]

#     while heap:
#         node = heapq.heappop(heap)
#         if distance[node[1]] == -1 or distance[node[1]] >= node[0]:
#             distance[node[1]] = node[0]

#             if node[1] in targets:
#                 routes[node[1]] = routes.get(node[1], []) + [node[2]]

#             for next in linked[node[1]]:
#                 if distance[next[1]] == -1 or distance[next[1]] >= next[0]+node[0]:
#                     heapq.heappush(heap, (next[0]+node[0], next[1], node[2].union([(node[1], next[1])])))


# T = int(sys.stdin.readline())

# for _ in range(T):
#     n, m, t = map(int, sys.stdin.readline().split())        # 교차로, 도로, 목적지 개수
#     s, g, h = map(int, sys.stdin.readline().split())        # 출발지, 두개의 노드

#     linked = [[] for _ in range(n+1)]
#     routes = {}
#     distance = [-1] * (n+1)
#     answers = []

#     for _ in range(m):
#         a, b, d = map(int, sys.stdin.readline().split())
#         linked[a].append((d, b))
#         linked[b].append((d, a))

#     targets = {int(sys.stdin.readline()) for _ in range(t)}

#     solution(s, targets)

#     for target in sorted(targets):
#         for route in routes.get(target, []):
#             if (g, h) in route or (h, g) in route:
#                 answers.append(target)
    
#     print(*answers)