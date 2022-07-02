import sys
sys.stdin = open('input.txt')

def solution(start):
    stack = [start]             
    pick = []                               # 선택된 학생들

    while stack:
        node = stack.pop()
        if not visited[node]:               # 현재 학생을 확인해보지 않았다면
            visited[node] = 1               # 확인 체크
            pick.append(node)               # 선택된 학생 명단에 추가
            next = selects[node] - 1        # 다음 학생 추가
            stack.append(next)
    
    if next in pick:                        # 선택된 학생 명단에, 다음 학생이 포함되어 있다면
        return pick[pick.index(next):]      # 그 학생을 기준으로 사이클(팀)이 만들어짐
    return []                               # 팀이 안이루어졌으므로 빈 리스트 반환

T = int(sys.stdin.readline())                                   # 테스트 케이스 개수

for _ in range(T):
    N = int(sys.stdin.readline())                               # 학생의 수
    selects = list(map(int, sys.stdin.readline().split()))      # 각 학생별 선택한 학생 번호
    visited = [0] * N                                           # 학생 탐색 여부
    answer = set()                                              # 팀으로 이루어진 학생들 명단
    
    for i in range(N):  
        if not visited[i]:              # 아직 확인해보지 않은 학생일 때
            team = solution(i)          
            answer.update(team)         # 팀으로 이루어진 학생들은 명단에 추가

    print(N - len(answer))