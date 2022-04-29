import heapq

def solution(operations):
    deleted = {}                                    # 삭제된 숫자들 목록 => 삭제된 숫자 : 삭제된 횟수
    min_heap = []                                   # 최소힙
    max_heap = []                                   # 최대힙

    for op in operations:                           # 명령어 데이터
        cmd, num = op.split(' ')                    # 명령어 종류, 숫자

        if cmd == 'I':                              # 입력 명령일때, 최소힙과 최대힙에 모두 값 추가
            heapq.heappush(min_heap, int(num))
            heapq.heappush(max_heap, -int(num))
        else:
            if num == '1':                                          # 최대힙 삭제인 경우
                while max_heap and deleted.get(-max_heap[0], 0):    # 최대힙에 값이 있고, 최소힙에서 해당 숫자를 삭제한 기록이 있으면
                    poped = heapq.heappop(max_heap)                 # 최대힙의 값도 삭제
                    deleted[-poped] -= 1                            # 삭제된 목록에서 횟수 차감
                
                if max_heap:                                        # 최대힙에 값이 있다면
                    num = heapq.heappop(max_heap)                   # 최댓값 제거
                    deleted[-num] = 1                               # 삭제된 목록에 숫자 추가
            else:
                while min_heap and deleted.get(min_heap[0], 0):
                    poped = heapq.heappop(min_heap)
                    deleted[poped] -= 1
                
                if min_heap:
                    num = heapq.heappop(min_heap)
                    deleted[num] = 1
    

    while min_heap and deleted.get(min_heap[0], 0):         # 최소힙에 여전히 값이 있고, 현재 최솟값이 삭제된 이력이 있으면
        poped = heapq.heappop(min_heap)                     # 최솟값 삭제
        deleted[poped] -= 1                                 # 삭제된 목록에서 횟수 차감
    
    while max_heap and deleted.get(-max_heap[0], 0):
        poped = heapq.heappop(max_heap)
        deleted[-poped] -= 1

    if not min_heap:                    # 최솟값이 비어있다면, 모든 값이 제거되었으므로 0, 0 반환
        return [0, 0]
    return [-max_heap[0], min_heap[0]]  # 최댓값, 최솟값 반환

print(solution(["I 16","D 1"]))
print(solution(["I 7","I 5","I -5","D -1"]))