import sys
from collections import deque
sys.stdin = open('input.txt')

T = int(sys.stdin.readline())

for _ in range(T):
    N, K = map(int, sys.stdin.readline().split())                   # 건물의 개수, 건설 순서 규칙의 개수
    delays = [0] + list(map(int, sys.stdin.readline().split()))     # 건물을 짓기 위한 소요 시간
    linked = [[] for _ in range(N+1)]                               # 건설 순서
    needs = [0] * (N+1)                                             # 현재 건물을 짓기 위해 필요한 건물 개수
    dp = [0] * (N+1)                                                # 현재 건물을 짓는데 소요되는 최소 시간

    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        linked[X].append(Y)                                         # 현재 건물이 완성되면 건설할 수 있는 다음 건물 추가
        needs[Y] += 1                                               # 다음 건물이 짓기 위해 필요한 건물 개수 추가

    W = int(sys.stdin.readline())                                   # 목표 건물
    q = deque()                                                 
    for i in range(1, N+1):                                         # 건설하기 위해 필요한 건물 개수가 0개인 노드 탐색
        if not needs[i]:
            q.append(i)                                             # 탐색을 위한 큐에 추가
            dp[i] = delays[i]                                       # 시작 건물들의 건설 소요 시간 입력

    while q:
        node = q.popleft()
        for next in linked[node]:
            dp[next] = max(dp[node] + delays[next], dp[next])       # 다음 건물의 소요시간은 현재 건물까지 소요시간+다음건물 소요시간
                                                                    # 지금까지 기록된 다음 건물 소요시간 중 큰 값 저장
            needs[next] -= 1                                        # 다음 건물이 필요한 건물 수 하나 제거
            if not needs[next]:                                     # 다음 건물 건설이 가능해지면 큐에 추가
                q.append(next)

    print(dp[W])