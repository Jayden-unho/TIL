import sys
sys.setrecursionlimit(100000)
sys.stdin = open('input.txt')

def find(n):                # 정점이 속한 집단의 대표를 찾음
    if n != s[n]:
        s[n] = find(s[n])
    return s[n]

def union(x, y):            # 정점 x와 y를 합침
    s[find(x)] = find(y)

def solution():
    global answer

    edge_cnt, idx = 0, 0                # 정점이 모두 연결되었는지 확인을 위한 변수, 간선의 인덱스

    while edge_cnt != N-1:              # 정점이 모두 연결되지 않았으면
        x = linked[idx][1]              # 정점
        y = linked[idx][2]

        if find(x) != find(y):          # 서로 연결이 되어 있지 않으면
            union(x, y)                 # 두 정점을 연결
            answer += linked[idx][0]    # 정답 증가
            edge_cnt += 1
        idx += 1


N = int(sys.stdin.readline())           # 정점의 개수
info = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]     # 정점간 거리의 정보
s = list(range(N))                      # 정점이 어디에 속했는지 구분할 리스트
linked = []                             # 간선의 정보들
answer = 0

for i in range(N):                              # 주어진 정보를 반복하여 간선의 정보들을 저장
    for j in range(i+1, N):
        linked.append((info[i][j], i, j))
linked.sort()

solution()

print(answer)