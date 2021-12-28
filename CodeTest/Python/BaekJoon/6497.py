import sys
import heapq
sys.stdin = open('input.txt')


def kruskal(start):                                     # 힙을 이용한 크루스칼 알고리즘 구현
    global min_cost

    heap = [(0, start)]                                 # 최초 시작 지점 초기화

    while heap:
        node = heapq.heappop(heap)
        if not visited[node[1]]:                        # 아직 연결되지 않은 도착지인 경우
            visited[node[1]] = 1                        # 방문 처리
            min_cost += node[0]                         # 길이 연결되었으므로 유지 비용 추가
            for e in linked[node[1]]:                   # 길의 길이를 기준으로 하여 최소힙 
                heapq.heappush(heap, (e[0], e[1]))


while True:
    M, N = map(int, sys.stdin.readline().split())       # 집의 개수, 길의 개수
    linked = [[] for _ in range(M)]                     # 집들의 연결 관계 리스트
    visited = [0] * M                                   # 해당 집 방문 여부 저장하는 리스트
    total_cost = 0                                      # 모든 길을 연결했을때 드는 비용
    min_cost = 0                                        # 모든 집을 연결하는데 드는 최소한의 비용

    if not sum((M, N)):                                 # 테스트 케이스 종료
        break

    for _ in range(N):
        x, y, z = map(int, sys.stdin.readline().split())    # 출발 집, 도착 집, 길의 길이
        total_cost += z                                     # 길의 유지비용 추가
        linked[x].append((z, y))                            # 양방향으로 집 연결 관계 추가
        linked[y].append((z, x))

    kruskal(0)                                              # 0번 집부터 크루스칼 시작

    print(total_cost - min_cost)                            # 절약할 수 있는 최대 비용