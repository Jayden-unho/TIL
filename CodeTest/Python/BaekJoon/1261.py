import sys
import heapq
sys.stdin = open('input.txt')


def dijkstra():
    heap = [(0, 0, 0)]

    while not visited[N-1][M-1]:
        node = heapq.heappop(heap)
        if not visited[node[1]][node[2]]:
            visited[node[1]][node[2]] = 1
            distance[node[1]][node[2]] = node[0]
            for k in range(4):
                r = node[1] + dr[k]
                c = node[2] + dc[k]
                
                if 0 <= r < N and 0 <= c < M and not visited[r][c]:
                    heapq.heappush(heap, (distance[node[1]][node[2]]+int(maze[r][c]), r, c))


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

M, N = map(int, sys.stdin.readline().split())           # 가로 세로
maze = [list(sys.stdin.readline()) for _ in range(N)]

distance = [[1e10]*M for _ in range(N)]
visited = [[0]*M for _ in range(N)]

dijkstra()

print(distance[N-1][M-1])