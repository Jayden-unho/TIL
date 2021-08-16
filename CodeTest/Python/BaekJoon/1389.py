'''
BFS 이용하여 탐색, 층이 하나씩 들어갈때마다 카운트한다
사람별 케빈베이컨 수를 담는 리스트는 사람 번호와 케빈베이컨을 담는 리스트로 만든다
'''

import sys
from collections import deque



def bfs_func(start):
    stack = deque([start])
    visit = []
    result_list = [0 for x in range(n+1)]
    cnt = 1
    idx = 0

    while stack:
        node = stack.popleft()
        if node not in visit:
            visit.append(node)
            
            for e in n_list[node]:
                if result_list[e] == 0 and start != e:
                    result_list[e] = cnt
                stack.append(e)
        if idx == 0:
            cnt += 1
            idx = len(stack)
        
        idx -= 1
                    
    
    return result_list
                


n, m = map(int, sys.stdin.readline().split())
n_list = [[] for _ in range(n+1)]
answer = []

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    n_list[a].append(b)
    n_list[b].append(a)


for i in range(1, n+1):
    tmp_list = bfs_func(i)
    answer.append([i, sum(tmp_list)])

answer.sort(key=lambda x: (x[1], x[0]))
print(answer[0][0])