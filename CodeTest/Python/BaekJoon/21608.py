import sys
sys.stdin = open('input.txt')


def search_coor(y, x, func):
    for k in range(4):
        r = y + dr[k]
        c = x + dc[k]

        if 0 <= r < N and 0 <= c < N:
            func(r, c)


def get_coor_info(y, x, friends):
    def inner_func(r, c):
        if classes[r][c] == 0:
            result[1] += 1
        elif classes[r][c] in friends:
            result[0] += 1

    result = [0, 0, y, x]
    search_coor(y, x, inner_func)
    return tuple(result)


def get_score(y, x, friends):
    def inner_func(r, c):
        nonlocal cnt

        if classes[r][c] in friends:
            cnt += 1

    cnt = 0
    search_coor(y, x, inner_func)
    if not cnt:
        return 0
    return 10 ** (cnt-1)


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

N = int(sys.stdin.readline())
classes = [[0] * N for _ in range(N)]
students = [[] for _ in range(N**2+1)]
survey = [list(map(int, sys.stdin.readline().split())) for _ in range(N**2)]

for id, *friends in survey:
    visited = set()
    coors = set()

    for f in friends:
        if not students[f]:
            continue

        def inner_func(r, c):
            global coors, visited

            if not classes[r][c] and (r, c) not in visited:
                info = get_coor_info(r, c, set(friends))
                visited |= {(r, c)}
                coors |= {info}

        y, x, *_ = students[f]
        search_coor(y, x, inner_func)

    if not coors:
        for i in range(N):
            for j in range(N):
                if not classes[i][j]:
                    info = get_coor_info(i, j, set(friends))
                    coors |= {info}

    coors = sorted(coors, key=lambda x: (x[2], x[3]))
    coors = sorted(coors, key=lambda x: (x[0], x[1]), reverse=True)

    _, _, y, x = coors[0]
    classes[y][x] = id
    students[id] = (y, x, friends)

answer = 0
for i in range(N):
    for j in range(N):
        id = classes[i][j]
        friends = students[id][2]
        answer += get_score(i, j, set(friends))

print(answer)
