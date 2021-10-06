import sys
from pprint import pprint
sys.setrecursionlimit(10000)
sys.stdin = open('input.txt')


def dfs(y, x, color, type):
    for k in range(4):
        r = y + dr[k]
        c = x + dc[k]

        if 0 <= r < N and 0 <= c < N:
            if type == 'nomal' and color == image[r][c] and not nomal[r][c]:
                nomal[r][c] = nomal_answer
                dfs(r, c, color, type)

            elif type == 'weakness' and not weakness[r][c]:
                if color == 'R' or color == 'G':
                    if image[r][c] == 'R' or image[r][c] == 'G':
                        weakness[r][c] = weakness_answer
                        dfs(r, c, color, type)
                elif color == 'B' and image[r][c] == 'B':
                    weakness[r][c] = weakness_answer
                    dfs(r, c, color, type)

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

N = int(sys.stdin.readline())
image = [sys.stdin.readline() for _ in range(N)]

nomal = [[0]*N for _ in range(N)]
weakness = [[0]*N for _ in range(N)]

nomal_answer, weakness_answer = 1, 1

for i in range(N):
    for j in range(N):
        if not nomal[i][j]:
            nomal[i][j] = nomal_answer
            dfs(i, j, image[i][j], 'nomal')
            nomal_answer += 1

        if not weakness[i][j]:
            weakness[i][j] = weakness_answer
            dfs(i, j, image[i][j], 'weakness')
            weakness_answer += 1

print(nomal_answer-1, weakness_answer-1)