import sys
from collections import deque
sys.stdin = open('input.txt')

def solution(a, b):
    visited = [False] * N                   # 노드 방문 여부
    q = deque([a, b])                       # 큐, 초기에 시작할 두개의 노드

    while q:        
        node = q.popleft()
        if not visited[node]:               # 아직 탐색하지 않은 노드라면
            visited[node] = True            # 해당 노드 탐색 완료
            for next in linked[node]:       # 부모 노드 탐색
                q.append(next)
        else:                               # 이미 탐색한 노드라면, 공통 조상
            return node

T = int(sys.stdin.readline())               # 테스트 케이스 수

for _ in range(T):
    N = int(sys.stdin.readline())           # 노드의 개수
    linked = [[] for _ in range(N)]         # 연결 관계

    for _ in range(N-1):
        a, b = map(int, sys.stdin.readline().split())
        linked[b-1].append(a-1)                         # B 노드의 부모는 A 노드

    A, B = map(int, sys.stdin.readline().split())       # 탐색할 두개의 노드

    print(solution(A-1, B-1) + 1)           # 탐색 및 반환값 출력