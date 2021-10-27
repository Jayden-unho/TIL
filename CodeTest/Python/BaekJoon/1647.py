import sys
sys.stdin = open('input.txt')


def find_set(x):
    if x != s[x]:
        s[x] = find_set(s[x])
    return s[x]


def union(x, y):
    s[find_set(y)] = find_set(x)


def kruskal():
    global answer

    edge_cnt, idx = 0, 0

    while edge_cnt != N-2:
        x = linked[idx][0]
        y = linked[idx][1]

        if find_set(x) != find_set(y):
            union(x, y)
            edge_cnt += 1
            answer += linked[idx][2]
        idx += 1


N, M = map(int, sys.stdin.readline().split())
linked = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(M)], key=lambda x: x[2])
s = [x for x in range(N+1)]
answer = 0

kruskal()
print(answer)