import sys


def dfs_func(start):
    stack = [start]
    visit = []

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(connect_list[node])

    return set(visit)


n, m = map(int, sys.stdin.readline().split())
n_list = {x for x in range(1, n+1)}                     # 노드의 리스트
connect_list = [[] for _ in range(n+1)]

for _ in range(m):
    n1, n2 = map(int, sys.stdin.readline().split())
    connect_list[n1].append(n2)
    connect_list[n2].append(n1)

answer_cnt = 0
while n_list:
    tmp_set = dfs_func(list(n_list).pop())
    n_list = n_list.difference(tmp_set)
    answer_cnt += 1


print(answer_cnt)