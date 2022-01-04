import sys
import heapq
sys.stdin = open('input.txt')


def solution(start: int):                           # 다익스트라 탐색
    distance = [-1] * (N+1)                         # 출발지로부터 각 노드까지 거리
    heap = [(0, start)]                             # 최소힙 리스트, 출발점 세팅

    while heap:
        node = heapq.heappop(heap)
        if distance[node[1]] < 0:                   # 아직 안가본 길이면, 거기까지 가는 최소 거리 저장
            distance[node[1]] = node[0]
            for e in linked[node[1]]:
                heapq.heappush(heap, (distance[node[1]] + e[0], e[1]))
    return distance


N, E = map(int, sys.stdin.readline().split())           # 정점의 개수, 간선의 개수
linked = [[] for _ in range(N+1)]                       # 정점들 간에 연결 관계

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())    # 출발 정점, 도착 정점, 두 정점간 거리
    linked[a].append((c, b))                            # 정점 양방향 연결 관계 설정
    linked[b].append((c, a))

necessary = list(map(int, sys.stdin.readline().split()))    # 꼭 방문해야할 정점 리스트

dis_init = solution(1)                      # 1번 정점에서 각 정점으로의 거리 구함

if dis_init[necessary[0]] >= 0 and dis_init[necessary[1]] >= 0:     # 꼭 방문해야하는 두 정점을 갈 수 있다면
    dis_1 = solution(necessary[0])          # 꼭 방문할 첫번째 정점에서 다른 정점으로의 거리
    dis_2 = solution(necessary[1])          # 두번쨰 정점에서 다른 정점으로의 거리

    # 1 -> 정점1 -> 정점2 -> N 과 1 -> 정점2 -> 정점1 -> N 으로 가는 두가지 방법 중 더 짧은 거리 출력
    print(min(dis_init[necessary[0]] + dis_1[necessary[1]] + dis_2[N], dis_init[necessary[1]] + dis_2[necessary[0]] + dis_1[N]))
else:
    print(-1)