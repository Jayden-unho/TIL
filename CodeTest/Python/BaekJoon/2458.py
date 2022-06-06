import sys
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())                       # 학생의 수, 학생 비교 횟수
distance = [[0] * N for _ in range(N)]                              # 학생들 키 비교 배열
answer = 0                                  

for _ in range(M):
    short, tall = map(int, sys.stdin.readline().split())            # 키 비교한 정보를 2차원 배열에 기록
    distance[short-1][tall-1] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if distance[i][k] == 1 and distance[k][j] == 1:         # i 보다 k 가 크고, k 보다 j 가 크면
                distance[i][j] = 1                                  # i 보다 j 가 크다

for i in range(N):
    cnt = sum(distance[i])                          # 현재 학생보다 키가 큰 학생의 수
    for j in range(N):                              # 현재 학생보다 키가 작은 학생의 수
        cnt += distance[j][i]
    if cnt == N-1:                                  # 키 크거나 작은 학생들이 모두 있을때 정답 케이스 1 증가
        answer += 1

print(answer)

# for _ in range(M):
#     short, tall = map(int, sys.stdin.readline().split())
#     distance[short-1][tall-1] = 1
#     distance[tall-1][short-1] = -1

# for k in range(N):
#     for i in range(N):
#         for j in range(N):
#             if (distance[i][k] != 1e10 and distance[k][j] != 1e10) and distance[i][j] == 1e10:
#                 distance[i][j] = distance[i][k] + distance[k][j]

# pprint(distance)