import sys
from collections import deque
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())       # 건물 수
linked = [[] for _ in range(N)]     # 각 건물이 완성되면 지을 수 있는 건물 목록
need = [0] * N                      # 건물 짓는데 필요한 앞 건물 개수
times = [0] * N                     # 건물 짓는데 소요 시간
answers = [0] * N                   # 건물 완성 시간

for idx in range(N):
    infos = list(map(int, sys.stdin.readline().split()))

    times[idx] = infos[0]               # 해당 건물 짓는데 소요 시간
    for i in range(1, len(infos)-1):
        linked[infos[i]-1].append(idx)  # 해당 건물을 짓기 위해 필요한 건물 기록
        need[idx] += 1                  # 건물 짓는데 필요한 앞 건물 개수 추가

q = deque()
for idx in range(N):                    # 앞 건물 없이 바로 지을 수 있으면
    if not need[idx]:                   # 큐에 추가
        q.append(idx)
        answers[idx] = times[idx]

while q:
    node = q.popleft()    
    for next in linked[node]:
        # 다음 건물 짓는데 필요한 건물 수 감소
        need[next] -= 1
        # 다음 건물 총 소요시간은 현재 건물 시간 + 다음 건물 시간
        answers[next] = max(answers[next], answers[node] + times[next])
        # 다음 건물을 짓기 위해 필요한 건물을 모두 지었다면, 큐에 추가
        if not need[next]:
            q.append(next)

for i in range(N):
    print(answers[i])