import heapq

def solution(jobs):
    N = len(jobs)                                       # 평균을 구하기 위한 작업의 개수
    heapq.heapify(jobs)                                 # 작업들을 최소힙으로 만듦
    ms = 0                                              # 현재 작업의 시간
    answer = 0                                          # 순수 작업한 시간

    waiting = []                                        # 작업 대기 명단
    while jobs or waiting:                              # 작업이 남아있으면 반복
        while jobs:                                     # 작업이 남아있다면
            task = heapq.heappop(jobs)               
            if task[0] > ms:                            # 현재 작업 요청된 시간의 이전일때
                heapq.heappush(jobs, task)              # 아직 작업 시작 못하므로 다시 작업 내역에 추가
                if not waiting:                         # 대기 명단이 비어 있으면 시간 1ms 흐르기
                    ms += 1
                break
            else:
                heapq.heappush(waiting, (task[1], task[0]))     # 작업이 가능하다면 대기명단에 추가
        
        if waiting:                                     # 대기명단에 작업이 있으면
            task = heapq.heappop(waiting)               # 가장 빨리 끝나는 작업 꺼내기
            answer += ms - task[1] + task[0]            # 작업 소요 시간 추가
            ms += task[0]                               # 작업이 끝났을때 시간으로 정의
    
    return answer//N                                    # 평균

print(solution([[0, 3], [1, 9], [2, 6]]))