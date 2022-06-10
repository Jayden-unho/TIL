import sys
sys.stdin = open('input.txt')

def initial_chk():                              # 입력의 표가 모든 도시의 최소 이동 시간이 맞는지 확인을 위한 함수
    prev_sum = [sum(r) for r in distance]       # 초기 표의 행별 합을 담은 리스트
    
    for k in range(N):                          # 최소 거리 확인을 위한 플로이드 워셜
        for i in range(N):
            for j in range(N):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    
    after_sum = [sum(r) for r in distance]      # 플로이드 워셜을 통해 최소 거리를 구한 정보

    for i in range(N):
        if prev_sum[i] != after_sum[i]:         # 행 하나라도 합이 다르다면
            return False                        # 입력의 표가 모든 도시의 최소 이동시간이 아님
    return True

def road_chk(i, j):                             # 두 도시를 잇는 도로를 제거해도 괜찮은지 확인을 위한 함수
    prev = distance[i][j]                       # 현재 두 도시의 최소 거리를 저장
    distance[i][j] = 1e10                       # 두 도시의 최소 거리 제거 (두 도시를 잇는 직선 거리를 제거)
    
    for k in range(N):                          # 두 도시를 다른 도시를 통해 이동했을때 최소 거리 구하기
        distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

    if prev != distance[i][j]:                  # 이전의 최소 거리가 이후의 최소 거리와 다르다면
        distance[i][j] = prev                   # 두 도시를 잇는 직선거리가 최소 거리이므로
        road.append((i, j))                     # 필요한 도로에 추가


N = int(sys.stdin.readline())                                                   # 도로의 개수
distance = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]     # 입력으로 주어진 도시간 최소 거리
road = []                                                                       # 필요한 직선 도로의 리스트

if not initial_chk():               # 입력으로 주어진 정보가 올바른 정보인지 확인
    print(-1)                       # 잘못된 입력이라면 -1 출력
else:
    for i in range(N):              
        for j in range(i+1, N):
            road_chk(i, j)          # 두 도시를 잇는 도로가 필요한 것인지 확인

    cnt = 0                         # 도로의 합
    for y, x in road:               # 필요한 도로의 거리를 더하기
        cnt += distance[y][x]

    print(cnt)