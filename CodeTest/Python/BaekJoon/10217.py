import sys
import heapq
sys.stdin = open('input.txt')

def solution():
    h = [(0, 0, 0)]                                                 # 초깃값
    distance = [[1e10] * (M+1) for _ in range(N)]                   # 행 - 도시, 열 - 거리

    while h:
        d, c, v = heapq.heappop(h)                                  # 소요시간, 비용, 도착 도시

        for next in linked[v]:
            next_d = next[0] + d                                    # 다음 도시 가는데 소요 시간
            next_c = next[1] + c                                    # 다음 도시 가는데 발생 비용
            
            if next_c <= M and next_d < distance[next[2]][next_c]:  # 비용이 한도를 넘지 않고, 최소거리일때
                for j in range(next_c, M+1):                        # 다음 비용부터 한도비용까지
                    if next_d >= distance[next[2]][j]:
                        break
                    distance[next[2]][j] = next_d                   # 다음 소요 시간이 최소 소요시간이 됨
                heapq.heappush(h, (next_d, next_c, next[2]))        # 다음 탐색

    return distance[-1][-1]

T = int(sys.stdin.readline())

for _ in range(T):
    N, M, K = map(int, sys.stdin.readline().split())            # 공항 수, 지원 비용, 티켓 정보 수
    linked = [[] for _ in range(N)]                             # 도시별 항공편

    for _ in range(K):
        u, v, c, d = map(int, sys.stdin.readline().split())     # 출발, 도착, 비용, 소요시간
        linked[u-1].append((d, c, v-1))                         # 단방향
    
    answer = solution()

    if answer != 1e10:          # 출력
        print(answer)
    else:
        print('Poor KCM')