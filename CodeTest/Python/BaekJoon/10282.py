import sys
import heapq
sys.stdin = open('input.txt')

def dijkstra(start):                        # 다익스트라
    now_time = 0                            # 현재 시간, 시작은 0으로 초기화
    h = [(now_time, start)]                 # 해킹됬을 당시 시간, 해킹 당한 컴퓨터 번호
    visited = [0] * N                       # 컴퓨터 감염 여부

    while h:
        node = heapq.heappop(h)
        if not visited[node[1]]:            # 아직 감염되지 않았다면
            now_time = node[0]              # 현재 시간을 감염이 완료되는 시간으로 변경
            visited[node[1]] = 1            # 해당 컴퓨터 감염 기록
            for next in linked[node[1]]:                            # 현재 컴퓨터를 의존하는 다른 컴퓨터 감염
                heapq.heappush(h, (next[0] + now_time, next[1]))    # 현재 시간 + 감염까지 걸리는 시간을 기록

    return sum(visited), now_time           # 감염된 컴퓨터의 개수, 마지막 컴퓨터가 감염이 완료되는 시간

T = int(sys.stdin.readline())               # 테스트 케이스 개수

for _ in range(T):
    N, D, C = map(int, sys.stdin.readline().split())        # 컴퓨터 개수, 의존성 개수, 해킹 당한 컴퓨터 개수
    linked = [[] for _ in range(N)]                         # 컴퓨터간 의존성 정보

    for _ in range(D):
        a, b, s = map(int, sys.stdin.readline().split())    # 컴퓨터 a, b 와 감염되는데 소요되는 시간
        linked[b-1].append((s, a-1))                        # 컴퓨터 b 감염되면, s 시간 이후 a 감염
    
    print(*dijkstra(C-1))                   # 다익스트라 이용하여 탐색

