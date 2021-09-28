import sys
from itertools import combinations
sys.stdin = open('input.txt')


def dfs(start, which):                                      # 각 선거구안에 있는 구역들이 서로 연결되어 있는지 확인
    stack = [start]
    cnt = 1                                                 # 해당하는 구역들만 돌았는지 확인용
    visited[start] = 1                                      # 처음 시작점 방문 처리

    while stack:
        node = stack.pop()
        for e in linked[node]:                              # 해당 구역에서 연결 되어 있는 곳들 반복
            if e in which and not visited[e]:               # 다음 연결된 곳이 방문하지 않았고, 같은 선거구에 속하는경우
                visited[e] = 1                              # 다음 구역 방문 처리
                stack.append(e)                
                cnt += 1                                    # 같은 선거구 내 다른 구역 방문 카운트
                    
    if cnt == len(which):                                   # 같은 선거구의 구역을 모두 돌았으면
        return True                                         # True 반환
    else:
        return False


N = int(sys.stdin.readline())
people = [0] + list(map(int, sys.stdin.readline().split()))     # 구역별 사람들 수 (0번 인덱스는 관리 편하게 하기 위해 추가)
linked = {}                                                     # 구역들 연결 관계
answer = 10**4                                                  # 선거구 간의 인구 차이 (조건에 의하면 N - 10 / 각 인구수  - 100 으로 최대 10^3)

for i in range(1, N+1):                                         # 구역별 연결 관계 정리
    num, *num_list = map(int, sys.stdin.readline().split())
    linked[i] = linked.get(i, []) + num_list
# print('LOG ----- LINKED : {}'.format(linked))

for k in range(1, (N//2 + 1)):                                  # 선거구가 최소 1개 이상이 되어야 하므로, 1부터 시작
                                                                # 선거구가 예를들어 총 7개 구역을 나눌때 (3, 4) 와 (4, 3) 는 같고, (2, 5) 와 (5, 2) 는 같으므로 7//2 까지만 반복
    part_1 = combinations(range(1, N+1), k)                     # 첫번째 선거구가 k개일때 경우의 수
    for one in part_1:                                          # one - 첫번째 선거구 / two - 두번째 선거구
        two = tuple(set(range(1, N+1)).difference(set(one)))    # 서로 반대이므로 차집합
        visited = [0] * (N+1)
        # print('LOG ----- ONE : {}, TWO : {}'.format(one, two))

        if dfs(one[0], one) and dfs(two[0], two):               # 두 선거구 모두가 구역들이 모두 이어져 있으면
            tmp_answer = 0                                      # 인구수 산출 위한 임시변수
            for o in one:                                       # 1번 선거구 총 인구수
                tmp_answer += people[o]
            
            for t in two:                                       # 1번 인구수 에서 2번 선거구 총 인구수를 뺀다 (차이)
                tmp_answer -= people[t]
            
            if answer > abs(tmp_answer):                        # 최소 차이 갱신시 변수에 저장
                answer = abs(tmp_answer)

if answer == 10**4:     # 최소 차이 없으면 -1 반환
    print(-1)
else:
    print(answer)