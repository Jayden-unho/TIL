import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())                                                       # 집의 개수
answer = 1e10                                                                       # 비용 (초기 최댓값)

# 색을 칠하는 비용을 기록하는 DP
# 0 ~ 2 인덱스 : 빨간색으로 시작해서 빨간색, 초록색, 파란색으로 끝나는 경우 
# 3 ~ 5 인덱스 : 초록색 시작
# 6 ~ 8 인덱스 : 파란색 시작

for i in range(N):                                              
    rgb = list(map(int, sys.stdin.readline().split()))                              # 색상을 입력 받음

    if not i:                                                                       # 첫 집일 경우
        dp = [1e10] * 9                                                             # 모든 경우 최댓값으로 설정
        for k in (0, 4, 8):                                                         # RGB 각 색상으로 시작하는 집은 비용 입력
            dp[k] = rgb[k%3]
    else:
        pre = dp[:]                                                                 # 이전까지 칠한 비용들 복사
        for k in range(9):                                                              
            dp[k] = rgb[k%3] + min(pre[(k+1)%3 + k//3*3], pre[(k+2)%3 + k//3*3])    # 현재 칠하려는 색상과 다른 색으로 칠한 이전 집들 중 작은 값을 더함

print(min(*dp[1:4], *dp[5:8]))              # 시작과 마지막에 같은 색인 경우 - 인덱스 1, 4, 8 을  제외한 값들 중 최솟값