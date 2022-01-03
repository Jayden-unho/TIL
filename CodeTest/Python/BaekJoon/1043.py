import sys
sys.stdin = open('input.txt')


def solution(person: list):                                 # 진실을 아는 사람들 구하는 함수 (진실을 아는 사람들)
    visited = [0] * (N+1)                                   # 사람 확인했는지 체크용 리스트

    stack = list(person.copy())
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = 1
            for e in linked[node]:                          # 현재 사람과 접촉한 사람들
                if e not in truth and not visited[e]:       # 진실을 모르고, 아직 확인하지 않은 사람이면
                    stack.append(e)                         # 스택에 추가, 진실을 아는 명단에 추가
                    truth.add(e)



N, M = map(int, sys.stdin.readline().split())                   # 사람 수, 파티의 개수
cnt_truth, *truth = map(int, sys.stdin.readline().split())      # 진실을 아는 사람 수, 진실을 아는 명단
linked = [set() for _ in range(N+1)]                            # 사람들 접촉 관계
parties = []                                                    # 파티 리스트
answer = 0                                                      # 정답 변수

for _ in range(M):
    cnt_person, *person = map(int, sys.stdin.readline().split())    # 현재 파티의 사람 수, 파티에 참여한 사람 명단

    parties.append(set(person))                                     # 파티 리스트에 참여한 사람 추가
    while cnt_person > 1:                                           # 파티에 2명 이상 참여했을때, 접촉 관계 추가
        linked[person[cnt_person-1]].add(person[cnt_person-2])
        linked[person[cnt_person-2]].add(person[cnt_person-1])
        cnt_person -= 1

truth = set(truth)                      # 진실을 아는 사람 중복 제거 위함

solution(truth)                         # 진실을 아는 모든 사람 구하기

for party in parties:                   # 파티에 진실을 아는 사람이 한명도 없으면 정답 개수 증가
    if not truth.intersection(party):
        answer += 1

print(answer)                           # 출력