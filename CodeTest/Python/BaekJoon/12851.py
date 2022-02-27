import sys
import heapq
sys.stdin = open('input.txt')

def solution(start):
    heap = [(0, start)]
    cnt = 0

    while heap:
        node = heapq.heappop(heap)
        if distance[node[1]] >= node[0]:
            distance[node[1]] = node[0]
            if node[1] == K:
                cnt += 1
            if node[1] - 1 >= 0:
                heapq.heappush(heap, (node[0]+1, node[1]-1))
            if node[1] + 1 <= 100000:
                heapq.heappush(heap, (node[0]+1, node[1]+1))
            if node[1] * 2 <= 100000:
                heapq.heappush(heap, (node[0]+1, node[1]*2))
    return cnt

N, K = map(int, sys.stdin.readline().split())
distance = [1e10] * 100001

answer = solution(N)

print(distance[K])
print(answer)