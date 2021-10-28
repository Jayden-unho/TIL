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

    idx, edge_cnt = 0, 0
    while edge_cnt != N-1:
        x = stack[idx][1]
        y = stack[idx][2]

        if find_set(x) != find_set(y):
            union(x, y)
            edge_cnt += 1
            answer += stack[idx][0]
        idx += 1


N = int(sys.stdin.readline())
planets = enumerate([list(map(int, sys.stdin.readline().split())) for _ in range(N)], 0)
s = [x for x in range(N)]
stack = []
answer = 0

for i in range(3):
    planets = sorted(planets, key=lambda x: x[1][i])
    for j in range(N-1):
        stack.append((abs(planets[j][1][i] - planets[j+1][1][i]), planets[j][0], planets[j+1][0]))

stack.sort(key=lambda x: x[0])
kruskal()
print(answer)