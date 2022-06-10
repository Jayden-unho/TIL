import sys
sys.stdin = open('input.txt')

N, K = map(int, sys.stdin.readline().split())                   # 사건의 수, 사건 비교 수
history = [[0] * N for _ in range(N)]                           # 사건 순서 정보

for _ in range(K):
    before, after = map(int, sys.stdin.readline().split())      
    history[before-1][after-1] = 1                              # 이전 사건, 이후 사건 = 1 을 지정하여 순서 표시

for k in range(N):
    for i in range(N):
        for j in range(N):
            if history[i][k] and history[k][j]:                 # i 이후 k가 발생하고, k 이후 j가 발생했다면
                history[i][j] = 1                               # i 이후 j가 발생

S = int(sys.stdin.readline())                                   # 확인하려는 사건 비교 수

for _ in range(S):
    s1, s2 = map(int, sys.stdin.readline().split())             # 사건1, 사건2
    
    if history[s1-1][s2-1]:             # 사건1 이후 사건2 발생하면
        print(-1)                       # -1 반환
    elif history[s2-1][s1-1]:           # 사건2 이후 사건1 발생하면
        print(1)                        # 1 반환
    else:                               # 사건의 전후관계를 모르면
        print(0)                        # 0 반환