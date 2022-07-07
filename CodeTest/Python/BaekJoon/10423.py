import sys
import heapq
sys.stdin = open('input.txt')

def solution(h):
    while h:
        w, n = heapq.heappop(h)                         # 가중치, 도시 번호
        if visited[n] == -1:                            # 전기가 연결되어 있지 않으면
            visited[n] = w                              # 사용한 케이블 가중치 기록
            for next in linked[n]:                      # 연결된 도시들
                heapq.heappush(h, (next[0], next[1]))   # 케이블 가중치, 다음 도시 번호


N, M, K = map(int, sys.stdin.readline().split())        # 도시, 케이블, 발전소 수
station = list(map(int, sys.stdin.readline().split()))  # 발전소 도시들 리스트
linked = [[] for _ in range(N)]                         # 도시간 연결 케이블 정보
visited = [-1] * N                                      # 도시들 전기 연결 여부

h = []                                                  # 최소 힙
for s in station:                                       # 발전소가 있는 도시들
    heapq.heappush(h, (0, s-1))                         # 가중치 0으로 처음 전기가 시작 되는곳

for _ in range(M):
    u, v, w = map(int, sys.stdin.readline().split())

    linked[u-1].append((w, v-1))                        # 케이블은 양방향으로 설치 가능하여
    linked[v-1].append((w, u-1))                        # 두개의 도시에 연결 정보 추가

solution(h)                         # 탐색

print(sum(visited))                 # 도시 케이블 연결된 가중치 합