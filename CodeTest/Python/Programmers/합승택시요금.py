import heapq

def solution(n, s, a, b, fares):    
    answer = 0                                          # 최소 요금
    linked = [[] for _ in range(n+1)]                   # 도로 정보들
    start_distance = []                                 # 시작 지점에서 각 지점으로 이동하는데 필요한 요금

    for fare in fares:                                  # 양방향으로 도로 정보를 저장함
        linked[fare[0]].append((fare[2], fare[1]))      # (도착지점, 요금)
        linked[fare[1]].append((fare[2], fare[0]))
    
    def dijkstra(start):
        distance = [-1] * (n+1)                         # 각 지점까지 거리를 -1로 초기 설정
        heap = [(0, start)]

        while heap:
            if distance[a] >= 0 and distance[b] >= 0:   # a지점과 b지점으로 이동하는 요금을 구했다면 종료
                if start == s:                          # 시작 지점에서 출발한 경우, 모든 지점으로의 요금 반환
                    return distance
                return distance[a], distance[b]         # 나머지 지점의 출발지는 a 지점과 b 지점으로의 요금 반환
            node = heapq.heappop(heap)
            if distance[node[1]] == -1:                 # 아직 확인되지 않은 지점인 경우
                distance[node[1]] = node[0]             # 요금 정보 갱신
                for e in linked[node[1]]:                           # 다음 도착지까지 이동하는 요금 추가
                    heapq.heappush(heap, (node[0] + e[0], e[1]))

    start_distance = dijkstra(s)                        # 시작 지점에서 처음 출발하여 각 지점으로 이동하는데 필요한 요금을 모두 구함
    answer = start_distance[a] + start_distance[b]      # 시작 지점에서 각자 a, b 지점으로 택시를 이용하는 경우
    for i in range(1, n+1):
        if i != s and start_distance[i] != -1:          # 시작 지점과 시작지점과 연결되지 않은곳은 탐색하지 않음
            res_a, res_b = dijkstra(i)                  # 해당 지점에서 a, b 지점으로 이동하는데 필요한 요금
            answer = min(answer, res_a + res_b + start_distance[i])     # 이전의 경우와, 시작 -> 현재 지점 까지는 같이 택시 이용하고,  나머지는 각자 택시 타는 경우를 비교하여 더 최솟값 저장

    return answer

print(solution(6, 4, 6, 2, 	[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
print(solution(6, 4, 5, 6, [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]))