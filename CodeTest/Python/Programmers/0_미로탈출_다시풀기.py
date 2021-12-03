"""
다익스트라
"""
import heapq

def dijkstra(start, end, linked_start, linked_end, traps, distance):
    heap = [(0, start, linked_start, linked_end)]

    while not distance[end]:
        node = heapq.heappop(heap)
        distance[node[1]] = node[0]

        if node[1] in traps:
            tmp_start = node[2][node[1]][:]
            tmp_end = node[3][node[1]][:]
            node[2][node[1]].clear()
            node[3][node[1]].clear()
            
            node[2][node[1]].extend(tmp_end)
            node[3][node[1]].extend(tmp_start)

        for e in node[2][node[1]]:
            heapq.heappush(heap, (distance[node[1]] + e[0], e[1], node[2], node[3]))
    
    return distance[end]


def solution(n, start, end, roads, traps):      # 개수, 시작, 도착, 경로, 함정
    linked_start = [[] for _ in range(n+1)]     # 연결 정보
    linked_end = [[] for _ in range(n+1)]
    distance = [0 for _ in range(n+1)]          # 최소 거리
    
    for e in roads:
        s, e, weight = e
        linked_start[s].append((weight, e))
        linked_end[e].append((weight, s))

    answer = dijkstra(start, end, linked_start, linked_end, set(traps), distance)

    return answer


print(solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2]))
print(solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]))