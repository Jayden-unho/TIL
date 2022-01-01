import sys
import heapq
sys.stdin = open('input.txt')


T = int(sys.stdin.readline())                                   # 테스트 케이스 개수

for _ in range(T):
    K = int(sys.stdin.readline())                               # 명령의 개수
    min_heap, max_heap = [], []                                 # 최소힙, 최대힙으로 사용할 리스트
    deleted = [0] * (K+1)                                       # 삭제된 숫자들 목록 리스트 (0-삭제되지 않음, 1-삭제됨)

    for i in range(K):
        command, num = sys.stdin.readline().split()             # 명령어 종류, 숫자
        num = int(num)

        if command == 'I':                                      # 삽입 연산
            heapq.heappush(min_heap, (num, i))                  # 최소힙과 최대힙에 모두 추가
            heapq.heappush(max_heap, (-num, i))                        

        elif command == 'D' and max_heap:                       # 삭제 연산
            if num == -1:                                       # 최소힙 삭제인 경우
                while min_heap and deleted[min_heap[0][1]]:     # 최소힙에 값이 남아있고, 현재 최솟값의 인덱스가 최대힙에서 삭제된 인덱스이면 삭제
                    heapq.heappop(min_heap)
                if min_heap:                                    # 여전히 최소힙이 남아있으면
                    node = heapq.heappop(min_heap)              # 최솟값 삭제
                    deleted[node[1]] = 1                        # 삭제한 최솟값의 인덱스를 삭제 처리

            else:                                               # 최대힙 삭제인 경우
                while max_heap and deleted[max_heap[0][1]]:     # 최대힙에 값이 남아있고, 현재 최댓값의 인덱스가 최소힙에서 삭제된 인덱스이면 삭제
                    heapq.heappop(max_heap)                             
                if max_heap:                                    # 최대힙이 남아있으면
                    node = heapq.heappop(max_heap)              # 최댓값 삭제 및 방금 삭제한 최댓값의 인덱스 삭제 처리
                    deleted[node[1]] = 1

    while min_heap and deleted[min_heap[0][1]]:                 # 최소힙에서 최솟값이 최대힙에서 삭제됬으면 삭제
        heapq.heappop(min_heap)                                
    while max_heap and deleted[max_heap[0][1]]:                 # 최대힙에서 최댓값이 최소힙에서 삭제됬으면 삭제
        heapq.heappop(max_heap)

    if not min_heap:                                            # 출력
        print('EMPTY')
    else:
        print(-heapq.heappop(max_heap)[0], heapq.heappop(min_heap)[0])