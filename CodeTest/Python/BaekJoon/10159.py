import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())               # 물건의 개수
M = int(sys.stdin.readline())               # 물건 비교한 횟수
order = [[0] * N for _ in range(N)]         # 물건들 간 무게 순서 정보

for _ in range(M):
    light, heavy = map(int, sys.stdin.readline().split())   # 가벼운 것, 무거운 것
    order[light-1][heavy-1] = 1                             # 가벼운 물건 뒤에 무거운 물건이 오므로 1 로 지정

for k in range(N):
    for i in range(N):
        for j in range(N):
            if order[i][k] and order[k][j]:     # i 보다 k 가 무겁고, k 보다 j 가 무거운 경우
                order[i][j] = 1                 # i 보다 j 가 무거우므로 1 지정

for i in range(N):                  # 해당 물건 번호의 행과 열에서 1 인 경우
    cnt = sum(order[i])             # 무게 비교가 되는 물건이므로
    for j in range(N):
        cnt += order[j][i]
    print(N-cnt-1)                  # N 개의 물건에서 1의 개수를 뺌 (1을 추가적으로 빼는건 자기 자신도 빼야하므로)