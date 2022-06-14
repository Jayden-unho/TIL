import sys
sys.stdin = open('input.txt')

def solution(node, ans):            # 현재 사람 번호, 탐색 깊이
    global answer

    if ans >= 5:                    # ABCDE 관계가 된다면
        answer = True               # 정답 변경
        return

    visited[node] = 1               # 현재 사람 탐색 체크

    for next in linked[node]:       # 현재 사람과 친구인 사람들 탐색
        if not visited[next]:       
            solution(next, ans+1)   # 아직 탐색하지 않은 사람이면, 다음 단계 탐색
    
    visited[node] = 0               # 현재 사람 탐색 해제

N, M = map(int, sys.stdin.readline().split())       # 사람, 친구 관계 수
linked = [[] for _ in range(N)]                     # 사람간 친구 관계
visited = [0] * N                                   # 탐색 여부
answer = False                                      # ABCDE 존재 여부

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    linked[a].append(b)                             # 친구 관계 연결
    linked[b].append(a)

for k in range(N):              # 0번부터 탐색
    solution(k, 1)

    if answer:                  # ABCDE 관계가 있다면
        print(1)                # 1 출력
        break
else:                           # 관계가 없다면, 0 출력
    print(0)