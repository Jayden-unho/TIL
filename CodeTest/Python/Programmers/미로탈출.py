import heapq


def dijkstra(start, end, linked_start, linked_end, traps, distance):
    heap = [(0, start)]

    while not distance[end]:
        print(heap)
        node = heapq.heappop(heap)
        distance[node[1]] = node[0]

        if node[1] in traps:
            for e in linked_start[node[1]]:
                linked_end[e[1]].append((e[0], node[1]))
            linked_start[node[1]].clear()

        for e in linked_start[node[1]]:
            heapq.heappush(heap, (distance[node[1]] + e[0], e[1]))
    
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