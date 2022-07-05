import sys
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())       # 가수, 보조PD 수
next = [[] for _ in range(N)]                       # 각 가수 다음에 순서와야 하는 가수
need = [0] * N                                      # 가수 순서 오기 위해 필요한 앞 사람 수
answers = []                                        # 정답

for _ in range(M):
    singers = list(map(int, sys.stdin.readline().split()))

    for idx in range(1, len(singers)-1):                # PD가 정한 가수 순서 확인
        next[singers[idx]-1].append(singers[idx+1]-1)   # 뒤에 올 가수 번호 추가
        need[singers[idx+1]-1] += 1                     # 앞에 필요한 가수 수 추가

q = []
for singer in range(N):
    if not need[singer]:
        q.append(singer)        # 바로 순서 정할 수 있는 가수 탐색

while q:
    node = q.pop()
    answers.append(node)        # 가수 순서 답안 기록

    for n in next[node]:        # 현재 가수의 다음 순서인 가수들 탐색
        need[n] -= 1            # 다음 가수의 필요한 앞 가수 수 감소
        if not need[n]:         # 앞 가수들이 모두 완료했다면
            q.append(n)         # 현재 가수 순서 추가

if not sum(need):               # 모든 가수가 순서를 정할 수 있다면
    for a in answers:           # 출력
        print(a+1)
else:                           # 한명이라도 순서가 안되는 경우
    print(0)