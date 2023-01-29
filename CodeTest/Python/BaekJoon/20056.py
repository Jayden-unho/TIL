import sys
sys.stdin = open('input.txt')

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

N, M, K = map(int, sys.stdin.readline().split())
fireballs = {}

for idx in range(M):
    r, c, m, s, d = map(int, sys.stdin.readline().split())
    fireballs[(r, c)] = [(m, s, d)]

while K > 0:
    new_fireballs = {}

    # 파이어볼 이동
    for k, v in fireballs.items():
        for m, s, d in v:
            nr = (k[0] + dr[d] * s) % N
            nc = (k[1] + dc[d] * s) % N

            new_fireballs[(nr, nc)] = new_fireballs.get(
                (nr, nc), []) + [(m, s, d)]

    # 중복되는 파이어볼 합체
    for k, v in new_fireballs.items():
        if len(v) == 1:
            continue

        new_m, new_s, directions = 0, 0, set()
        for m, s, d in v:
            new_m += m
            new_s += s
            directions.add(d % 2)
        new_m //= 5
        new_s //= len(v)

        new_fireballs[k] = []
        if not new_m:
            continue
        elif len(directions) == 1:
            for d in range(0, 7, 2):
                new_fireballs[k].append((new_m, new_s, d))
        else:
            for d in range(1, 8, 2):
                new_fireballs[k].append((new_m, new_s, d))

    # 새로운 좌표
    fireballs = new_fireballs
    K -= 1

answer = 0
for v in fireballs.values():
    for m, s, d in v:
        answer += m

print(answer)
