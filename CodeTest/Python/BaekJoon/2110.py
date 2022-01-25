import sys
sys.stdin = open('input.txt')

N, C = map(int, sys.stdin.readline().split())                   # 집의 개수, 공유기의 개수
home = sorted([int(sys.stdin.readline()) for _ in range(N)])    # 집의 위치
answer = 0

l, r = 1, home[-1] - home[0]            # 공유기간의 거리 최솟값과 최댓값
while l <= r:
    gap = (l+r) // 2                    # 공유기간 거리 중간부터 해서 탐색
    pre = home[0]                       # 처음 공유기를 설치하는 집을 기준으로 최초 선택
    cnt = 1                             # 공유기 설치한 집의 개수

    for i in range(1, N):
        if home[i] - pre >= gap:        # 이전에 설치한 집과 현재 집의 거리가 기준 보다 멀다면
            cnt += 1                    # 집의 개수 증가
            pre = home[i]               # 이전 집 변수에 현재 집 위치 넣기
        
        if cnt >= C:                    # 공유기 개수가 조건의 개수 이상이라면
            l = gap + 1                 # 거리를 늘려서 공유기 개수를 줄이기 위함
            answer = gap                # 정답에 현재 거리를 저장
            break
    else:               
        r = gap - 1         # 공유기 개수가 부족하다면, 거리를 줄이기

print(answer)