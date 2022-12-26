import sys
import heapq
sys.stdin = open('input.txt')


def dijkstra():
    h = [(0, 1, {1})]

    while h:
        # 거리, 노드, 경로
        dist, node, paths = heapq.heappop(h)
        # 거리가 같거나 적을때만
        if distances[node] >= dist:
            # 현재 도착지점이고, 친구 위치를 지났다면 True 반환
            if node == V and P in paths:
                return True
            distances[node] = dist
            for next_dist, next_node in linked[node]:
                sum_dist = next_dist + dist
                # 다음 이동이 최소가 아니면 힙에 추가하지 않음
                if distances[next_node] < sum_dist:
                    continue
                heapq.heappush(h, (sum_dist, next_node, paths | {next_node}))
    return False


V, E, P = map(int, sys.stdin.readline().split())
linked = [[] for _ in range(V+1)]
distances = [1e10] * (V+1)

# 간선 정보 추가
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    linked[a].append((c, b))
    linked[b].append((c, a))

# 다익스트라 탐색
if dijkstra():
    print('SAVE HIM')
else:
    print('GOOD BYE')
