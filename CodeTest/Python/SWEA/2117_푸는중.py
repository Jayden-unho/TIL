"""
최소한 이득을 봐야함 - 모든 
"""


import sys
sys.stdin = open('input.txt')

    


dr = [-1, 0 ,1 ,0]
dc = [0, 1, 0, -1]

T = int(input())
answer = []

for tc in range(1, T+1):
    N, M = map(int, input().split())        # length of array / cost each home
    village = [list(map(int, input().split())) for _ in range(N)]

    cost = {}
    home = {}

    for i in range(N):
        for j in range(N):
            if village[i][j]:
                home[(i, j)] = 1
    
    k = 0
    res = 0
    while res < M * len(home):
        cost[k] = res
        k += 1
        res = k*k + (k-1)*(k-1)

    for i in range(N):
        for j in range(N):
            for z in range(k-1, 0, -1):
                dfs(i, j, z)