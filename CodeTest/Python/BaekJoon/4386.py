"""
python
    Memory - 29 mb
    Time - 68 ms
"""

import sys
from itertools import combinations
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
    while edge_cnt < N-1:
        x = linked[idx][0]
        y = linked[idx][1]

        if find_set(x) != find_set(y):
            union(x, y)
            edge_cnt += 1
            answer += linked[idx][2]
        idx += 1


N = int(sys.stdin.readline())
stars = enumerate([list(map(float, sys.stdin.readline().split())) for _ in range(N)])

s = [x for x in range(N)]
linked = []
answer = 0

for e in combinations(stars, 2):
    weight = (((e[0][1][0]-e[1][1][0])**2)+((e[0][1][1]-e[1][1][1])**2)) ** 0.5
    linked.append((e[0][0], e[1][0], weight))

linked.sort(key=lambda x: x[2])

kruskal()

print(answer)