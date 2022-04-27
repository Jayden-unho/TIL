import heapq

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def solution(land, height):
    def dfs(y, x):                                                          # DFS 탐색
        nonlocal visited_cnt

        stack = [(y, x)]                                                    # 시작 좌표

        while stack:
            node = stack.pop()
            if not visited[node[0]][node[1]]:                               # 아직 방문하지 않은 좌표일때
                visited[node[0]][node[1]] = 1                               # 방문 처리
                visited_cnt += 1                                            # 방문한 좌표들 개수 카운트 추가

                for k in range(4):                                          # 상하좌우 인접 좌표
                    r = node[0] + dr[k]
                    c = node[1] + dc[k]

                    if 0 <= r < N and 0 <= c < N:
                        dif = abs(land[node[0]][node[1]] - land[r][c])      # 인접한 좌표와의 높이 차이
                        if dif <= height:                                   # 사다리 없이 이동 가능하면 스택에 좌표 추가
                            stack.append((r, c))
                        else:                                               # 사다리 필요하다면 높이 차이 값과 좌표를 최소힙에 기록
                            heapq.heappush(h, (dif, r, c))

    N = len(land)                           # 2차원 배열 길이
    answer = 0                              # 사다리 이용 비용
    visited_cnt = 0                         # 방문한 좌표 카운트

    visited = [[0] * N for _ in range(N)]   # 방문 여부 리스트
    h = [(0, 0, 0)]                         # 최소힙, 초기값은 높이 차이 0, 좌표 0,0

    while visited_cnt < N**2:               # 아직 다 방문하지 않았다면
        diff, y, x = heapq.heappop(h)       # 최소힙에서 높이 차이가 가장 작은 좌표 가져옴
        if not visited[y][x]:               # 방문하지 않은 좌표인 경우에만 탐색
            answer += diff                  # 사다리 이용 비용 추가
            dfs(y, x)

    return answer

print(solution([[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]], 3))
print(solution([[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]], 1))