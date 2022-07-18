import sys
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())                   # 집하장 수, 경로 수
dp = [[1e10] * N for _ in range(N)]                             # 두 집하장간 최단 경로
answer = [['-'] * N for _ in range(N)]                          # 먼저 이동해야하는 집하장 번호

for _ in range(M):
    a, b, t = map(int, sys.stdin.readline().split())            # 집하장 a, b, 이동 시간
    a -= 1                  
    b -= 1
    dp[a][b], dp[b][a] = t, t                                   # 두 집하장 이동에 소요되는 시간
    answer[a][b], answer[b][a] = b, a                           # 먼저 이동해야하는 집하장 번호 기록

for k in range(N):                                              # 중간에 거치는 집하장
    for i in range(N):
        for j in range(N):
            # i, j, k 가 모두 다르며, 중간에 k 집하장을 거쳐 가는게 더 빠를때
            if i != j != k and dp[i][j] > dp[i][k] + dp[k][j]:
                dp[i][j] = dp[i][k] + dp[k][j]                  # 최소 시간 갱신
                answer[i][j] = answer[i][k]                     # 처음 이동할 집하장이므로
                                                                # i에서 k로 이동시 처음 이동하는 집하장 기록

for i in range(N):                          # 출력
    for j in range(N):
        if answer[i][j] == '-':
            print('-', end=' ')
        else:
            print(answer[i][j]+1, end=' ')
    print()