import sys
sys.stdin = open('input.txt')


def solution(start: int):                                               # 벨만포드 (시작 노드)
    dist[start] = 0                                                     # 시작 위치의 거리는 0으로 세팅
    
    for i in range(1, N+1):                                             # 도시의 개수만큼 반복하여 확인
        for j in range(1, N+1):                                         # 모든 도시들의 버스 경로 확인 (모든 간선 확인)
            for e in linked[j]:
                if dist[j] != 1e10 and dist[e[1]] > dist[j] + e[0]:     # 시작 지점이 무한대가 아니고, 새로운 거리가 더 짧을때
                    dist[e[1]] = dist[j] + e[0]                         # 새로운 거리 갱신

                    if i == N:                                          # N번 확인했을때도 계속 값 갱신이 일어난다면 무한 반복
                        return True
    return False


N, M = map(int, sys.stdin.readline().split())           # 도시 개수, 버스 경로 개수
linked = [[] for _ in range(N+1)]                       # 버스 경로들 저장할 리스트
dist = [0] + [1e10] * N                                 # 어떠한 도시에서 특정 도시들로 향하는 거리

for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().split())    # 버스 경로들 출발지점, 도착지점, 거리
    linked[A].append((C, B))
    

if solution(1):             # 계속 무한히 반복이면 -1 출력
    print(-1)
else:
    for d in dist[2:]:
        if d == 1e10:       # 갈수없는 도시라면 -1 출력
            print(-1)
        else:
            print(d)