import sys
from collections import deque
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())           # 학생의 수, 키를 비교한 횟수
linked = [[] for _ in range(N+1)]                       # 각 학생들의 본인보다 키 큰 학생의 목록
need = [0] * (N+1)                                      # 각 학생들의 본인보다 키 작은 학생의 수
answer = []                                             # 정답

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())       
    linked[a].append(b)                                 # 키 작은 학생 기준, 키 큰 학생 이름 기록
    need[b] += 1                                        # 키 큰 학생 기준으로 키 작은 학생 수 추가

q = deque()                             # 줄 서야하는 명단     
for i in range(1, N+1):
    if not need[i]:                     # 학생들을 한번씩 확인하여 키가 작아서
        q.append(i)                     # 가장 앞에 나와야 하는 모든 학생들 추가

while q:                                # 학생들이 아직 줄을 서지 않았다면
    node = q.popleft()

    for next in linked[node]:           # 현재 학생보다 키가 큰 학생들은
        need[next] -= 1                 # 키 작은 학생의 수 하나씩 뺌
        if need[next] <= 0:             # 키 큰 학생의 앞에 있는 키 작은 학생들이 모두 줄을 섰으면 줄서는 명단에 추가
            q.append(next)
    
    answer.append(node)                 # 현재 학생 줄 세우기

print(*answer)