import sys
sys.stdin = open('input.txt')


def solution(start):                            # DFS 탐색
    stack = [start]
    visited[start] = 1                          # 첫 시작점 방문처리

    while stack:
        node = stack.pop()
        for i in linked[node]:                  # 인접한 노드 탐색
            if visited[i] == visited[node]:     # 인접한 곳이 서로 같은 숫자인 경우, 이분 그래프가 성립하지 않음
                return False
            elif not visited[i]:                # 인접한 곳이 아직 방문하지 않은 경우
                visited[i] = -visited[node]     # 서로 다른 방문 처리
                stack.append(i)                 # 스택에 인접 노드 추가
    return True

K = int(sys.stdin.readline())                       # 테스트 케이스 개수

for _ in range(K):
    V, E = map(int, sys.stdin.readline().split())   # 노드 개수, 간선 개수
    linked = [[] for _ in range(V+1)]               # 연결 관계
    visited = [0] * (V+1)                           # 방문처리하는 리스트

    for _ in range(E):
        u, v = map(int, sys.stdin.readline().split())   # 연결관계 정리, 양방향
        linked[u].append(v)
        linked[v].append(u)

    for i in range(1, V+1):         # 노드들이 하나의 그래프로만 존재하지 않을수도 있음
        if not visited[i]:          # 확인하지 않은 노드라면, 탐색
            if not solution(i):
                print('NO')
                break
    else:                           # 모든 노드들이 이분 그래프를 만족하면, YES 출력
        print('YES')