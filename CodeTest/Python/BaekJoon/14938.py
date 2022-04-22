import sys
import heapq
sys.stdin = open('input.txt')

def solution(start, m):                                             # 다익스트라 (시작 노드 번호, 수색 범위)
    global answer

    distance = [-1] * (N+1)                                         # 다른 노드까지의 거리
    h = [(0, start)]                                                # 거리, 시작 노드
    ans = 0                                                         # 현재 경우의 최대 아이템 개수 카운트 변수

    while h:
        node = heapq.heappop(h)
        if distance[node[1]] == -1:                                 # 이동하지 않은곳이면
            distance[node[1]] = node[0]                             # 이동 표시
            if node[0] <= m:                                        # 수색 범위 내의 노드라면
                ans += items[node[1]]                               # 아이템 개수 카운트 추가
                for next in linked[node[1]]:                        # 연결된 다음 노드 탐색
                    heapq.heappush(h, (next[0]+node[0], next[1]))
    
    answer = max(answer, ans)                                       # 기존에 구한 다른 정답과 비교하여 최대값 저장

N, M, R = map(int, sys.stdin.readline().split())                    # 노드의 개수, 수색 범위, 간선의 개수
items = [0] + list(map(int, sys.stdin.readline().split()))          # 아이템 개수 정보들
linked = [[] for _ in range(N+1)]                                   # 노드간 연결 정보
answer = 0                                                          # 정답 변수

for _ in range(R):
    a, b, l = map(int, sys.stdin.readline().split())                # 시작 노드, 도착 노드, 거리
    linked[a].append((l, b))                                        # 양방향 저장
    linked[b].append((l, a))

for i in range(1, N+1):                                             # 1번 노드부터 모든 노드 탐색
    solution(i, M)

print(answer)