# 내장 모듈 사용 (heapq 는 최소힙만 가능하여, 최대 힙을 구현할시 살짝 응용이 필요함)
# import sys
# import heapq



# N = int(sys.stdin.readline())
# h = []

# for _ in range(N):
#     x = int(sys.stdin.readline())

#     if not x:
#         if not h:
#             print(0)
#         else:
#             print(-1 * heapq.heappop(h))
#     else:
#         heapq.heappush(h, -x)




# 직접 구현함 / 시간초과
# import sys
# from collections import deque



# def push(item):
#     heap.append(item)
#     push_sort(len(heap)-1)

# def pop():
#     if is_empty():
#         return 0
    
#     tmp = heap.popleft()

#     if not is_empty():
#         heap.appendleft(heap.pop())
#         pop_sort(0)

#     return tmp

# def is_empty():
#     return not heap

# def pop_sort(idx):
#     while idx < len(heap):
#         if (idx*2 + 2) < len(heap) and heap[idx] < max(heap[(idx*2) + 1], heap[(idx*2) + 2]):
#             if heap[(idx*2) + 1] >= heap[(idx*2) + 2]:
#                 heap[idx], heap[(idx*2) + 1] = heap[(idx*2) + 1], heap[idx]
#                 idx = (idx*2) + 1
#             else:
#                 heap[idx], heap[(idx*2) + 2] = heap[(idx*2) + 2], heap[idx]
#                 idx = (idx*2) + 2
        
#         if (idx*2 + 1) < len(heap) and heap[idx] < heap[(idx*2) + 1]:
#             heap[idx], heap[(idx*2) + 1] = heap[(idx*2) + 1], heap[idx]

# def push_sort(idx):
#     while idx > 0:
#         if heap[idx] > heap[(idx-1)//2]:
#             heap[(idx-1)//2], heap[idx] = heap[idx], heap[(idx-1)//2]
#             idx = (idx-1)//2



# N = int(sys.stdin.readline())
# heap = deque()

# for _ in range(N):
#     x = int(sys.stdin.readline())

#     if not x:
#         print(pop())
#     else:
#         push(x)