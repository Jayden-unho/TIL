from collections import deque

def solution(people, limit):
    answer = 0
    q = deque(sorted(people, reverse=True))     # 사람의 무게를 내림차순으로 정렬

    while q:                                    # 사람이 남아있으면
        answer += 1                             # 보트 한개 추가
        if len(q) < 2:                          # 한명만 남았으면, 혼자 사용
            q.pop()
        elif q[0] + q[-1] <= limit:             # 무게가 가장 작은 사람과 가장 큰 사람이 같이 타도 괜찮으면
            q.pop()                             # 둘이 같이 탑승
            q.popleft()
        else:                                   # 둘이 탑승이 불가능하다면, 몸무게 큰 사람이 혼자 탑승
            q.popleft()

    return answer

print(solution([70, 50, 80, 50]	, 100))
print(solution([70, 80, 50]	, 100))