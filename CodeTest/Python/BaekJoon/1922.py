""" 
kruskal 이용

Memory - 52 mb
Time - 0.336 s
"""


import sys
sys.stdin = open('input.txt')


# kruskal
def find_set(x):
    if x != s[x]:
        s[x] = find_set(s[x])
    return s[x]


def union(x, y):
    s[find_set(y)] = find_set(x)


def kruskal():
    global answer

    edge_cnt, idx = 0, 0

    while edge_cnt != N-1:
        x = linked[idx][0]
        y = linked[idx][1]

        if find_set(x) != find_set(y):
            union(x, y)
            edge_cnt += 1
            answer += linked[idx][2]
        idx += 1


N = int(sys.stdin.readline())       # 컴퓨터 개수
M = int(sys.stdin.readline())       # 연결할 수 있는 선의 개수
s = [x for x in range(N+1)]                 # 컴퓨터간의 연결 관계

linked = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(M)], key=lambda x: x[2])
answer = 0


kruskal()
print(answer)