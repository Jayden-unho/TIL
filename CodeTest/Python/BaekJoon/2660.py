import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())                           # 사람 수
answers = [[1e10] * N for _ in range(N)]                # 사람들 가까운 정도

while True:
    a, b = map(int, sys.stdin.readline().split())       

    if a == -1:                                         # 입력이 음수이면 종료
        break
    
    answers[a-1][b-1] = 1                               # 두 사람은 친구 관계로 거리 1
    answers[b-1][a-1] = 1

for k in range(N):
    answers[k][k] = 0                                   # 본인은 거리 0으로 설정
    for i in range(N):
        for j in range(N):
            # 두 사람의 직접 관계와 누군가를 통하는 관계 중 더 짧은 거리 선택
            answers[i][j] = min(answers[i][j], answers[i][k] + answers[k][j])

min_length = 1e10                   # 가장 작은 회원 점수
min_li = set()                      # 회장 후보
for i in range(N):
    l = max(answers[i])             # 한 사람의 회원 점수

    if min_length < l:              # 회원 점수가 전체 최소값 보다 크다면
        continue                    # 다음 사람 탐색
    elif min_length > l:            # 최소값 갱신시 회장 후보 모두 제거
        min_li.clear()
        min_length = l
    min_li.add(i+1)                 # 회장 후보 추가

print(min_length, len(min_li))      # 출력
print(*sorted(min_li))