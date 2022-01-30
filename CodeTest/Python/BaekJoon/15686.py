import sys
from itertools import combinations
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())                               # 도시의 크기, 최대 치킨집의 개수
city = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]     # 도시의 정보 / 0-빈칸, 1-집, 2-치킨집

chicken = []        # 치킨집의 좌표들
home = []           # 집의 좌표들
answer = 1e10       # 도시의 치킨 거리, 초기에 임의의 큰 값

for i in range(N):                      # 도시를 한번 확인하여, 치킨집과 집의 좌표들을 모두 구함
    for j in range(N):
        if city[i][j] == 1:
            home.append((i+1, j+1))
        elif city[i][j] == 2:
            chicken.append((i+1, j+1))

dist = [[0] * len(home) for _ in range(len(chicken))]       # 각 치킨집별 집까지의 치킨 거리 / 행-치킨집의 번호, 열-집의 번호

for i in range(len(chicken)):
    for j in range(len(home)):
        dist[i][j] = abs(chicken[i][0] - home[j][0]) + abs(chicken[i][1] - home[j][1])  # i번째 치킨집과 j번째 집의 치킨 거리를 구하여 저장

for comb in combinations(range(len(chicken)), M):       # 조합을 이용하여 치킨집을 M개 선택
    tmp = 0                                             # 현재 경우의 도시의 치킨 거리
    for h in range(len(home)):                          # 모든 집의 치킨 거리를 구해야 함
        min_dist = 1e10
        for c in comb:                                  
            min_dist = min(min_dist, dist[c][h])        # 선택한 치킨 거리와 이전의 치킨 거리 중 최솟값을 저장 
        tmp += min_dist                                 # 도시의 치킨 거리에 현재 집의 치킨 거리 추가

        if tmp >= answer:           # 탐색하던 중 기존에 구해둔 도시의 치킨 거리 보다 큰 값이면, 이후에 찾아도 의미 없으므로 종료
            break
    else:
        answer = tmp                # 도시의 치킨 거리 최솟값 갱신
        
print(answer)                       # 출력
