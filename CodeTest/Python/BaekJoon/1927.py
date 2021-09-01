# # 힙 모듈 사용
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
#             print(heapq.heappop(h))
#     else:
#         heapq.heappush(h, x)