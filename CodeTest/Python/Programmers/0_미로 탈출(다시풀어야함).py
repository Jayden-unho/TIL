import heapq
import sys
sys.setrecursionlimit(100000)

def solution(n, start, end, roads, traps):      # 방의 개수, 출발 노드, 도착 노드, 간선 정보, 함정 노드 목록
    linked = [[[] for _ in range(n+1)] for _ in range(2**len(traps))]

    for p, q, s in roads:
        linked[0][p].append((s, q))

    print(linked)

    for i in range(1, 2**len(traps)):
        idx = 0
        while i:
            num = i % 2
            if num:
                node = traps[idx]
                for j in range(1, n+1):
                    for e in linked[0][j]:
                        if e[1] ==
            i //= 2
            idx += 1

    def dfs(linked):
        pass


    return

print(solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2]))
print(solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]))