import sys

N = int(sys.stdin.readline())   # 배열의 길이
K = int(sys.stdin.readline())   # 찾으려는 인덱스 번호
answer = 0                      # 정답

low, high = 0, K                # 정답의 최소 숫자, 최대 숫자
while low <= high:              # 이분탐색
    mid = (low+high) // 2       # 정답으로 올 현재 숫자 선택
    cnt = 0

    for i in range(1, N+1):     # 2차원 배열의 모든 행 탐색
        cnt += min(mid//i, N)   # 각 행에 현재 숫자보다 작은게 몇개인지 카운트
    
    if cnt >= K:                # K번째 이후의 숫자라면
        high = mid - 1          # 정답으로 작성
        answer = mid
    else:                       # K반째 숫자 이전이면
        low = mid + 1

print(answer)