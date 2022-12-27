import sys
from collections import deque
sys.stdin = open('input.txt')


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def get_distances(y, x):
    q = deque([(y,  x)])
    distances = [[-1] * W for _ in range(H)]
    distances[y][x] = 0

    while q:
        r, c = q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]

            if 0 <= nr < H and 0 <= nc < W and room[nr][nc] != 'x' and distances[nr][nc] == -1:
                distances[nr][nc] = distances[r][c] + 1
                q.append((nr, nc))

    return distances


def get_coors(room):
    start = ()
    dirty = set()

    for i in range(H):
        for j in range(W):
            if room[i][j] == 'o':
                start = (i, j)
            elif room[i][j] == '*':
                dirty.add((i, j))

    return start, dirty, set([start]) | dirty


def get_new_linked(y, x, coors):
    global answer
    linked = {}

    for r, c in coors:
        if y == r and x == c:
            continue
        elif distances[r][c] == -1:
            answer = -1
            return linked
        linked[(y,  x)] = linked.get((y, x), []) + [(distances[r][c], (r, c))]

    return linked


def DFS(n, ans, y, x):
    global answer

    if answer <= ans:
        return
    elif n == 0:
        answer = ans
        return

    for dist, (nr, nc) in linked[(y, x)]:
        if not visited.get((nr, nc), False):
            visited[(nr, nc)] = True
            DFS(n-1, ans+dist, nr, nc)
            visited[(nr, nc)] = False


while True:
    W, H = map(int, sys.stdin.readline().split())
    if not W and not H:
        break

    room = [list(sys.stdin.readline().rstrip()) for _ in range(H)]
    start, dirty, coors = get_coors(room)
    answer = 1e10

    linked = {coor: [] for coor in coors}
    for y, x in coors:
        distances = get_distances(y, x)
        new_linked = get_new_linked(y, x, coors)
        linked.update(new_linked)

    if answer == -1:
        print(-1)
    else:
        visited = {}
        visited[(start[0], start[1])] = True
        DFS(len(dirty), 0, *start)

        print(answer)
