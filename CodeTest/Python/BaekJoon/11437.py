import sys
sys.stdin = open('input.txt')

def set_parents():
    stack = [0]                                     # DFS 탐색 위한 스택
    visited[0] = 1                                  # 루트 노드 방문처리
    level[0] = 0                                    # 루트 노드 레벨 0

    while stack:
        node = stack.pop()
        for next in linked[node]:                   # 해당 노드와 연결된 노드 탐색
            if not visited[next]:                   # 방문 하지 않은 노드만
                visited[next] = 1
                parents[next] = node                # 연결된 노드의 부모는 현재 노드
                level[next] = level[node] + 1       # 연결된 노드의 레벨은 현재 노드 레벨 + 1
                stack.append(next)                  # 다음 탐색을 위한 노드 추가

def solution(a, b):
    while level[a] != level[b]:                     # 비교하는 두 노드의 레벨이 다르면
        if level[a] < level[b]:                     # B 노드가 레벨이 더 높으면 (루트로 부터 더 멀다면)
            b = parents[b]                          # B 노드 레벨 낮추기
        else:                                           
            a = parents[a]                          # A 노드 레벨 낮추기

    while a != b:                                   # 레벨이 같은데, 두 노드가 서로 다르다면
        a = parents[a]                              # 각각 부모 노드 가져오기
        b = parents[b]

    return a                                        # A와 B가 동일하므로 공통 부모 노드

N = int(sys.stdin.readline())                       # 노드의 개수
linked = [[] for _ in range(N)]                     # 노드의 연결 관계
parents = [-1] * N                                  # 각 노드의 부모 노드 번호
level = [-1] * N                                    # 각 노드의 트리 레벨(높이)
visited = [0] * N                                   # 노드 탐색 여부

for _ in range(N-1):                                # 노드들 연결 관계를 정리
    a, b = map(int, sys.stdin.readline().split())
    linked[a-1].append(b-1)
    linked[b-1].append(a-1)

set_parents()                                       # 루트 노드를 시작으로 탐색

M = int(sys.stdin.readline())                       # 비교할 노드들의 개수

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print(solution(a-1, b-1) + 1)                   # 두 노드의 공통 부모 찾기