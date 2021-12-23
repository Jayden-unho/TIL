import sys
import heapq
sys.stdin = open('input.txt')


N = int(sys.stdin.readline())   # 숫자 개수
heap = []                       # 힙으로 사용할 리스트
answer = 0                      # 정답 변수

for _ in range(N):              # 숫자들을 모두 최소힙에 푸시
    heapq.heappush(heap, int(sys.stdin.readline()))

while len(heap) > 1:                        # 최소힙 안에 2개 이상 있으면 반복
    node_1 = heapq.heappop(heap)            # 가장 작은 수
    node_2 = heapq.heappop(heap)            # 두번째로 작은 수
    answer += node_1 + node_2               # 정답에 더함
    heapq.heappush(heap, node_1 + node_2)   # 더한 수를 최소힙에 추가

print(answer)