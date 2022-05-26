import sys
import heapq as h
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
min_h = []                              # 최소힙
max_h = []                              # 최대힙

for _ in range(N):
    num = int(sys.stdin.readline())     # 들어갈 숫자

    if len(min_h) == len(max_h):        # 두개의 힙이 길이가 같다면, 우선 최소힙에 추가
        h.heappush(min_h, num)
    elif num > -max_h[0]:               # 새로 들어오는 숫자가 현재 중간값 보다 크면
        h.heappush(min_h, num)          # 최소힙에 추가
    else:                               # 새로 들어오는 숫자가 현재 중간값 보다 작거나 같으면
        h.heappush(max_h, -num)         # 최대힙에 추가
    
    if len(max_h) < len(min_h):         # 최소힙의 길이가 더 길면
        n = h.heappop(min_h)            # 최소힙의 제일 작은 값을 최대힙으로 이동
        h.heappush(max_h, -n)
    elif len(max_h) > len(min_h) + 1:   # 최대힙의 길이가 최소힙보다 2 이상 길면
        n = h.heappop(max_h)            # 최대힙의 최대값을 최소힙으로 이동
        h.heappush(min_h, -n)
    
    print(-max_h[0])                    # 최대힙의 최댓값(중간값)을 출력