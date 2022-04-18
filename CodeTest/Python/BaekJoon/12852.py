import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())                       # 찾으려는  수
dp = {0 : [], 1: [1]}                               # 각 숫자별 연산 순서 (최소만 기록)

for idx in range(1, N+1):                                                                               # 찾으려는 수까지 반복
    if idx * 3 <= N:                                                                                    # 3배수가 찾으려는 값을 넘지 않을때
        if (dp.get(idx*3, False) and len(dp[idx*3]) > len(dp[idx]) + 1) or not dp.get(idx*3, False):    # 현재 경우에서 연산하였을때 최소 횟수로 연산이거나, 다음 숫자가 아직 연산 기록이 없을 경우에
            dp[idx*3] = [idx*3] + dp[idx]                                                               # 다음 숫자에 연산 순서 기록

    if idx * 2 <= N:
        if (dp.get(idx*2, False) and len(dp[idx*2]) > len(dp[idx]) + 1) or not dp.get(idx*2, False):
            dp[idx*2] = [idx*2] + dp[idx]

    if idx + 1 <= N:
        if (dp.get(idx+1, False) and len(dp[idx+1]) > len(dp[idx]) + 1) or not dp.get(idx+1, False):
            dp[idx+1] = [idx+1] + dp[idx]

    dp.pop(idx-1)                                                                                       # 메모리 확보 위하여 이전에 사용한 참고값 제거

print(len(dp[N])-1)         # 출력
print(*dp[N])