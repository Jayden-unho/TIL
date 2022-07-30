import sys
import heapq
sys.stdin = open('input.txt')

def solution(start: int):                           # 다익스트라 탐색
    distance = [1e10] * (N+1)                         # 출발지로부터 각 노드까지 거리
    heap = [(0, start)]                             # 최소힙 리스트, 출발점 세팅
    
    while heap:
        dist, node = heapq.heappop(heap)
        if distance[node] > dist:                   # 아직 안가본 길이면, 거기까지 가는 최소 거리 저장
            distance[node] = dist
            for next in linked[node]:
                heapq.heappush(heap, (distance[node] + next[0], next[1]))
    return distance

N, E = map(int, sys.stdin.readline().split())           # 정점의 개수, 간선의 개수
linked = [[] for _ in range(N+1)]                       # 정점들 간에 연결 관계

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())    # 출발 정점, 도착 정점, 두 정점간 거리
    linked[a].append((c, b))                            # 정점 양방향 연결 관계 설정
    linked[b].append((c, a))

necessary = list(map(int, sys.stdin.readline().split()))    # 꼭 방문해야할 정점 리스트

dis_init = solution(1)                                      # 1번 정점에서 각 정점으로의 거리 구함

dis_1 = solution(necessary[0])                              # 꼭 방문할 첫번째 정점에서 다른 정점으로의 거리
dis_2 = solution(necessary[1])                              # 두번쨰 정점에서 다른 정점으로의 거리

# 출발지 -> n1 -> n2 -> 도착지와 출발지 -> n2 -> n1 -> 도착지 중 짧은 거리
ans = min(dis_init[necessary[0]] + dis_1[necessary[1]] + dis_2[N], dis_init[necessary[1]] + dis_2[necessary[0]] + dis_1[N])

# 경로 존재하지 않는다면 -1, 그 외 출력
if ans >= 1e10:
    print(-1)
else:
    print(ans)