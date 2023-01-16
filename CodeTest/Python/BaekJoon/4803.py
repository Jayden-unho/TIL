import sys
sys.stdin = open('input.txt')


def union(a, b):
    a = find(a)
    b = find(b)

    if a == b or a in cycles or b in cycles:
        cycles.add(a)
        cycles.add(b)

    groups[b] = a


def find(x):
    if x != groups[x]:
        groups[x] = find(groups[x])
    return groups[x]


TC = 0
while True:
    N, M = map(int, sys.stdin.readline().split())
    if N == 0 and M == 0:
        break

    groups = [i for i in range(N)]
    cycles = set()
    for _ in range(M):
        a, b = map(lambda x: int(x) - 1, sys.stdin.readline().split())
        union(a, b)

    for i in range(N):
        find(i)

    trees = len(set(groups) - cycles)

    TC += 1
    print(f'Case {TC}: ', end='')
    if not trees:
        print('No trees.')
    elif trees == 1:
        print('There is one tree.')
    else:
        print(f'A forest of {trees} trees.')
