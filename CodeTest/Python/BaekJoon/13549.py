import sys
import heapq
sys.stdin = open('input.txt')

def solution(start):        
    heap = [(0, start)]             # 처음에 시작은 0초, 처음에 출발하는 수빈이 위치
    
    while heap:
        if road[K] != -1:           # 동생한테 도착했다면 종료
            return
        node = heapq.heappop(heap)
        if 0 <= node[1] <= 100000 and road[node[1]] == -1:              # 다음에 움직일 곳이 범위 내이고, 아직 방문하지 않았으면
            road[node[1]] = node[0]                                     # 다음 위치에 소요되는 시간 기록
            heapq.heappush(heap, (road[node[1]] + 1, node[1] - 1))      # 1초가 걸려 이동하는 좌우 추가
            heapq.heappush(heap, (road[node[1]] + 1, node[1] + 1))
            heapq.heappush(heap, (road[node[1]], node[1] * 2))          # 0초가 걸려 이동하는 텔레포트 위치 추가

N, K = map(int, sys.stdin.readline().split())       # 수빈이의 위치, 동생의 위치
road = [-1] * 100001                                # 수빈이와 동생이 이동 가능한 영역

solution(N)         # 수빈이 위치를 기준으로 다익스트라 탐색

print(road[K])      # 출력