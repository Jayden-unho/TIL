import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())                                           # 행의 길이
dp = [[0] * 3 for _ in range(2)]                                        # 0행-최대, 1행-최소

for _ in range(N):      
    a, b, c = map(int, sys.stdin.readline().split())                    # 각 줄의 숫자값
    
    pre_max = dp[0][:]                                                  # 이전 줄의 최댓값들
    pre_min = dp[1][:]                                                  # 이전 줄의 최솟값들

    dp[0][0] = max(pre_max[0] + a, pre_max[1] + b)                      # 각 열의 나올 수 있는 경우들 중 최댓값 및 최솟값 저장
    dp[0][1] = max(pre_max[0] + a, pre_max[1] + b, pre_max[2] + c)
    dp[0][2] = max(pre_max[1] + b, pre_max[2] + c)

    dp[1][0] = min(pre_min[0] + a, pre_min[1] + b)
    dp[1][1] = min(pre_min[0] + a, pre_min[1] + b, pre_min[2] + c)
    dp[1][2] = min(pre_min[1] + b, pre_min[2] + c)

print(max(dp[0]), min(dp[1]))                                           # 출력