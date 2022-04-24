import heapq

def solution(n, edge):  
    linked = [[] for _ in range(n+1)]               # 노드의 연결 관계
    distance = [0] * (n+1)                          # 노드들의 거리

    for a, b in edge:                               # 노드 연결 관계 정리 (양방향)
        linked[a].append((1, b))
        linked[b].append((1, a))

    def dijkstra(start):                            # 다익스트라
        h = [(1, start)]                            # 시작 노드 입력

        while h:
            node = heapq.heappop(h)
            if not distance[node[1]]:               # 아직 확인 안한 노드이면
                distance[node[1]] = node[0]         # 거리 기록
                for next in linked[node[1]]:        # 다음 노드들 탐색
                    heapq.heappush(h, (node[0]+next[0], next[1]))

    dijkstra(1)
    max_distance = max(distance)                    # 가장 먼 거리 구하기
    answer = distance.count(max_distance)           # 가장 먼 거리에 있는 노드의 개수 세기
    return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))