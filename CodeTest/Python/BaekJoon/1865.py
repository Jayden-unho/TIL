import sys
sys.stdin = open('input.txt')


def solution():
    distance[1] = 0                                         # 출발 도시 거리는 0으로 초기화

    for i in range(1, N+1):                                 # 도시의 개수만큼 반복하여 확인
        for j in range(1, N+1):                             # 도로 및 웜홀의 개수만큼 반복
            for e in linked[j]:
                if distance[e[1]] > distance[j] + e[0]:     # 새로운 거리값이 더 짧은 거리값이라면 갱신
                    distance[e[1]] = distance[j] + e[0]

                    if i == N:                              # 도시의 개수만큼 반복하였는데, 계속 값이 바뀐다면
                        return True                         # 음의 무한 싸이클 존재
    return False


TC = int(sys.stdin.readline())                              # 테스트케이스 개수

for _ in range(TC):
    N, M, W = map(int, sys.stdin.readline().split())        # 도시의 개수, 경로의 개수, 웜홀 개수
    distance = [1e10] * (N+1)                               # 각 도시로 가는데 소요되는 거리(시간)
    linked = [[] for _ in range(N+1)]                       # 각 도시 연결 관계

    for _ in range(M):                                      # 도로
        S, E, T = map(int, sys.stdin.readline().split())    # 출발 도시, 도착 도시, 도시 소요 시간
        linked[S].append((T, E))                            # 도시 연결 관계 추가
        linked[E].append((T, S))

    for _ in range(W):                                      # 웜홀
        S, E, T = map(int, sys.stdin.readline().split())    # 출발 도시, 도착 도시, 돌아가는 시간
        linked[S].append((-T, E))
    
    if solution():          # 음수로 인해 무한 싸이클 발생하는 곳이 있다면, YES 출력
        print('YES')
    else:
        print('NO')