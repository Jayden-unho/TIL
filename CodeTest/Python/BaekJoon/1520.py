""" Memory - 41328 KB / Time - 192 ms """
# recursive dfs and memoization
import sys
sys.setrecursionlimit(5000)
sys.stdin = open('input.txt')


def backtracking_dfs(node):
    # Base Case
    if node[0] == M-1 and node[1] == N-1:
        return 1
    elif visited[node[0]][node[1]] != -1:
        return visited[node[0]][node[1]]


    visited[node[0]][node[1]] += 1
    
    for k in range(4):
        y = node[0] + dr[k]
        x = node[1] + dc[k]

        if 0 <= y < M and 0 <= x < N and mountain[node[0]][node[1]] > mountain[y][x]:
            visited[node[0]][node[1]] += backtracking_dfs((y, x))
    
    return visited[node[0]][node[1]]


M, N = map(int, sys.stdin.readline().split())
mountain = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

visited = [[-1] * N for _ in range(M)]
answer = 0

answer = backtracking_dfs((0,0))

print(answer)


# recursive dfs and backtracking
# Time Error
""" import sys
sys.setrecursionlimit(5000)
sys.stdin = open('input.txt')


def backtracking_dfs(node):
    global answer
    
    if node[0] == M-1 and node[1] == N-1:
        answer += 1
        return
    
    cnt_no_way = 0
    
    visited[node[0]][node[1]] = True

    for k in range(4):
        y = node[0] + dr[k]
        x = node[1] + dc[k]

        if 0 <= y < M and 0 <= x < N and mountain[node[0]][node[1]] > mountain[y][x] and not visited[y][x] and not no_way[y][x]:
            backtracking_dfs((y, x))
            visited[y][x] = False

            if no_way[y][x]:
                cnt_no_way += 1
        else:
            cnt_no_way += 1
            
    if cnt_no_way == 4:
        no_way[node[0]][node[1]] = True


M, N = map(int, sys.stdin.readline().split())
mountain = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

visited = [[False] * N for _ in range(M)]
no_way = [[False] * N for _ in range(M)]
answer = 0


backtracking_dfs((0,0))

print(answer) """