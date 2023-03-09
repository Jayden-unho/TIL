import sys
from itertools import permutations
from collections import deque
sys.stdin = open("input.txt")

dr = [-1, 0, 1, 0, 0, 0]
dc = [0, 1, 0, -1, 0, 0]
dh = [0, 0, 0, 0, 1, -1]


def BFS(floor, rotations):
    if boards[floor[-1]][rotations[-1]][4][4] == 0:
        return 1e10

    q = deque([(0, 0, 0)])
    visited = [[[-1] * 5 for _ in range(5)] for _ in range(5)]
    visited[0][0][0] = 0

    while q:
        h, r, c = q.popleft()
        if visited[h][r][c] + 1 >= answer:
            break

        for k in range(6):
            nh = h + dh[k]
            nr = r + dr[k]
            nc = c + dc[k]

            if 0 <= nh < 5 and 0 <= nr < 5 and 0 <= nc < 5 and visited[nh][nr][nc] == -1 and boards[floor[nh]][rotations[nh]][nr][nc] == 1:
                visited[nh][nr][nc] = visited[h][r][c] + 1
                q.append((nh, nr, nc))

    return visited[4][4][4] if visited[4][4][4] != -1 else 1e10


def rotate(li):
    return list(zip(*li[::-1]))


def make_cube(idx, rotations):
    global answer

    if idx > 0 and boards[permu[0]][rotations[0]][0][0] == 0:
        return
    elif idx == 5:
        answer = min(BFS(permu, rotations), answer)
        if answer == 12:
            print(answer)
            exit(0)
        return

    for ro in range(4):
        make_cube(idx+1, rotations + [ro])


boards = [[[list(map(int, sys.stdin.readline().split()))
            for _ in range(5)] for _ in range(1)] for _ in range(5)]
answer = 1e10

for i in range(5):
    pre = boards[i][0]
    for _ in range(3):
        pre = rotate(pre)
        boards[i].append(pre)

for permu in permutations(range(5), 5):
    make_cube(0, [])

print(answer if answer != 1e10 else -1)
