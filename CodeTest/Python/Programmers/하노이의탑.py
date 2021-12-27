def hanoi(n, start, middle, end, answer):       # 원반 개수(높이), 원반이 출발하는 기준 기둥, 중간 기둥, 목적지 기둥, 정답 리스트
    if n == 1:                                  # 현재 원반이 1층 높이(최상단이라 옮겨야 하는 경우)
        answer.append([start, end])             # 현재 기둥에서 목적지 기둥으로 옮김
        return
    
    hanoi(n-1, start, end, middle, answer)      # 지금 보고 있는 기둥에서 위에 원반선택, 목적지는 중간에 거쳐야 하는것으로 변경
    answer.append([start, end])                 # 위에 원반들을 모두 옮겼으니, 다음 원반 이동
    hanoi(n-1, middle, start, end, answer)      # 중간 기둥에 있는 원반을 옮기기 위해 재귀

def solution(n):
    answer = []                     # 원반 이동을 저장하는 리스트

    hanoi(n, 1, 2, 3, answer)       # 하노이 함수

    return answer


print(solution(3))