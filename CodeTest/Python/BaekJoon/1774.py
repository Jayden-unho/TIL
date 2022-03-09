import sys
import heapq
sys.stdin = open('input.txt')

def solution(start):
    global answer

    heap = [(0, start)]

    while heap:
        node = heapq.heappop(heap)                      
        if not visited[node[1]]:                        # 도착 노드를 아직 연결하지 않았으면
            visited[node[1]] = 1                        # 연결 처리
            answer += node[0]                           # 가중치(거리)를 정답에 누적
            for e in linked[node[1]]:                   # 도착 노드에서 다음 노드로 갈 수 있는 간선들 반복하여 확인
                heapq.heappush(heap, e)
        

N, M = map(int, sys.stdin.readline().split())           # 노드의 개수, 이미 연결된 간선의 개수
infos = []                                              # 노드들의 위치 좌표를 저장할 리스트
linked = [[] for _ in range(N+1)]                       # 간선 정보 리스트
visited = [0] * (N+1)                                   # 각 노드의 연결 여부
answer = 0                                              # 정답 변수

for _ in range(N):                                      # 노드들의 좌표값을 입력 받아서
    x, y = map(int, sys.stdin.readline().split())       # 리스트에 저장
    infos.append((x, y))

for _ in range(M):                                      # 두개의 노드가 이미 연결된 간선은
    n1, n2 = map(int, sys.stdin.readline().split())     # 가중치를 0으로 하여 간선 정보 저장
    linked[n1].append((0, n2))
    linked[n2].append((0, n1))

for i in range(len(infos)):                             # 각 노드의 좌표값들을 서로 비교
    for j in range(len(infos)):                         
        if i != j or not infos[i] or not infos[j]:      # 같은 노드가 아니고, 이미 연결된 노드가 아니면
            x1, y1 = infos[i]                       
            x2, y2 = infos[j]

            weight = ((x1-x2)**2 + (y1-y2)**2)**0.5     # 노드간 거리 계산 (가중치 계산)
            linked[i+1].append((weight, j+1))           # (가중치, 도착 노드) 순으로 간선 정보 저장
            
solution(1)                                             # 1번 노드부터 간선 연결 시작

print(f'{answer:.2f}')