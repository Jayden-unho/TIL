import sys
import heapq
from collections import deque
sys.stdin = open('input.txt')

N, K = map(int, sys.stdin.readline().split())                                                                   # 보석의 개수, 가방의 개수
gems = deque(sorted([list(map(int, sys.stdin.readline().split())) for _ in range(N)], key=lambda x: x[0]))      # 각 보석의 무게와 가격들을 보석의 무게순으로 오름차순
backpacks = sorted([int(sys.stdin.readline()) for _ in range(K)])                                               # 가방을 가벼운 순서대로 정렬
answer = 0

available = []                                      # 담을 수 있는 보석들
for backpack in backpacks:                          # 가벼운 가방부터 탐색 시작
    while gems and backpack >= gems[0][0]:          # 보석 리스트에 보석이 남아있고, 현재 가방에 들어갈 수 있다면
        heapq.heappush(available, -gems[0][1])      # 보석의 무게를 음수로 하여 저장 (heapq는 최소힙 -> 음수를 저장하여 최대힙으로 활용)
        gems.popleft()                              # 보석 리스트의 가장 앞의 보석을 삭제

    if available:                                   # 담을 수 있는 보석이 있다면
        answer += -heapq.heappop(available)         # 가장 가치가 높은 보석을 가방에 담음


print(answer)