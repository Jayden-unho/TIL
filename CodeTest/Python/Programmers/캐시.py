from collections import deque

def solution(cacheSize, cities):
    answer = 0                          # 정답 변수
    q = deque()                         # 캐시 공간

    if not cacheSize:                   # 캐시 사이즈가 0인 경우, 입력마다 항상 5초가 소요 됨
        return len(cities) * 5

    for city in cities: 
        city = str(city).lower()        # 대소문자 구분을 안함
        if city not in q:               # 현재 도시가 캐시 공간에 저장되어 있지 않으면
            if len(q) >= cacheSize:     # 캐시 공간이 꽉 차있으면 가장 사용안한 입력 제거
                q.popleft()
            q.append(city)              # 새로운 입력 추가
            answer += 5                 # 5초 증가
        else:
            q.remove(city)              # 캐시 공간에 이미 저장되어 있다면, 기존에 저장된 위치 제거
            q.append(city)              # 가장 최근 입력으로 다시 추가
            answer += 1                 # 1초 증가

    return answer


print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(0, ['la', 'la']))