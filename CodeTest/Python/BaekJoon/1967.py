"""
리프노드 - 리프노드  인 경우만 탐색 (이유: 루트나 중간 노드는 아래에 자식 노드가 있는데,
                                    가중치가 양의 정수이기에 자식 노드로 내려가면 더 긴 지름 생겨남)
"""


import sys
sys.setrecursionlimit(100000)
sys.stdin = open('input.txt')


def dfs(node, ans):
    global distance, start_node

    if ans > distance:
        distance = ans
        start_node = node

    for e in linked[node]:
        if not visited[e[1]]:
            visited[e[1]] = 1
            dfs(e[1], ans+e[0])


N = int(sys.stdin.readline())
linked = [[] for _ in range(N+1)]
visited = [0] * (N+1)
distance = 0
start_node = -1

for _ in range(N-1):
    start, end, weight = map(int, sys.stdin.readline().split())
    linked[start].append((weight, end))
    linked[end].append((weight, start))

visited[1] = 1
dfs(1, 0)

distance = 0
visited = [0] * (N+1)

visited[start_node] = 1
dfs(start_node, 0)

print(distance)