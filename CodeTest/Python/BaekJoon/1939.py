import sys
import heapq
sys.stdin = open('input.txt')


def solution(start):
    heap = [(-1e10, start)]                                             # 출발지에서는 최대한 무게, 출발지

    while heap:
        node = heapq.heappop(heap)                                      # 다음 목표지에 이동 가능한 최대 무게, 도착지
        if weights[node[1]] < -node[0]:                                 # 다음 도착지에 이동 가능한 무게 < 현재 다리를 이동해서 이동 가능한 무게
            weights[node[1]] = -node[0]                                 # 가능한 무게 새로 갱신

            for e in linked[node[1]]:                                   # 현재 섬에서 이동가능한 다리들 탐색
                if weights[e[1]] < -max(e[0], node[0]):                 # 목적지로 이동가능한 최대 무게보다 현재 위치에서 출발해 다리 이용시 이동 가능한 최대 무게가 더 큰 경우에만 heap 추가
                    heapq.heappush(heap, (max(e[0], node[0]), e[1]))    # 현재 섬까지 이동 가능한 최대 무게, 현재 섬에서 다음 섬으로 이동하는 다리가 견딜 수 있는 무게 중 더 가벼운거 중 최대값을 저장

N, M = map(int, sys.stdin.readline().split())                   # 섬의 개수, 다리의 개수
linked = [[] for _ in range(N+1)]                               # 섬의 연결 관계
weights = [0] * (N+1)                                           # 각 섬으로 한번에 이동가능한 최대 중량

for _ in range(M):                                              # 다리 정보
    A, B, C = map(int, sys.stdin.readline().split())            # 출발지, 도착지, 견딜 수 있는 무게
    linked[A].append((-C, B))                                   # 양방향이므로 출발지와 도착지에 기록, 최대힙을 이용하므로 중량을 음수의 값을 넣음
    linked[B].append((-C, A))

factory1, factory2 = map(int, sys.stdin.readline().split())     # 공장 출발지, 도착지

solution(factory1)          # 다익스트라 탐색

print(weights[factory2])    # 출력