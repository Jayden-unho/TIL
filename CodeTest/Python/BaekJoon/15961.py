import sys

N, D, K, C = map(int, sys.stdin.readline().split())     # 접시 수, 종류 수, 연속해서 먹는 수, 쿠폰 번호
sushi = []                  # 초밥들 목록
selected = [0] * (D+1)      # 초밥 종류별 선택 여부
selected[C] = 1             # 쿠폰 번호의 초밥 무조건 먹음
answer = 0                  

for _ in range(N):
    sushi.append(int(sys.stdin.readline()))             # 초밥 벨트의 정보

sushi.extend(sushi[:K-1])               # 초밥이 회전되므로 앞의 일부분을 뒤에 이어 붙임

ans = 1                                 # 쿠폰의 초밥은 항상 먹으므로 1로 시작
for i in range(N+K-1):
    s = sushi[i]                        # 현재 먹는 초밥 종류
    selected[s] += 1                    # 선택 +1
    if selected[s] == 1:                # 새로운 종류 먹는 경우
        ans += 1                        # 먹는 종류 개수 1 증가
    
    if i >= K-1:                        # 연속해서 먹기 시작하는 경우
                                        # (인덱스가 K-1일 때, 처음 연속해서 K개 먹게 됨)
        answer = max(answer, ans)       # 초밥 종류 많이 먹은 경우를 기록

        r = sushi[i-K+1]                # 다음 연속해서 K개 먹기 위해 앞에 제거될 초밥
        if r != C:                      # 쿠폰 초밥이 아닌 경우
            selected[r] -= 1            # 종류 선택 개수 -1
            if not selected[r]:         # 해당 종류 초밥을 안먹는 경우
                ans -= 1                # 먹는 종류 개수 -1

print(answer)