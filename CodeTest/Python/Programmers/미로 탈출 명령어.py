import sys
sys.setrecursionlimit(10000000)

dr = [1, 0, 0, -1]
dc = [0, -1, 1, 0]


def solution(n, m, x, y, r, c, k):
    answer = ''

    def sol(y, x, remain, ans):
        nonlocal answer

        if not remain:
            for i in range(len(ans)):
                if ans[i] == 0:
                    ans[i] = 'd'
                elif ans[i] == 1:
                    ans[i] = 'l'
                elif ans[i] == 2:
                    ans[i] = 'r'
                elif ans[i] == 3:
                    ans[i] = 'u'
            answer = ''.join(ans)
            return

        dist = abs(r-y) + abs(c-x)
        if dist > remain:
            answer = 'impossible'
            return
        elif dist == remain:
            horizon = c - x
            vertical = r - y

            if horizon >= 0 and vertical >= 0:
                # 오른쪽 아래
                sol(-1, -1, 0, ans + [0] * abs(vertical) + [2] * abs(horizon))
            elif horizon >= 0 and vertical < 0:
                # 오른쪽 위
                sol(-1, -1, 0, ans + [2] * abs(horizon) + [3] * abs(vertical))
            elif horizon < 0 and vertical >= 0:
                # 왼쪽 아래
                sol(-1, -1, 0, ans + [0] * abs(vertical) + [1] * abs(horizon))
            elif horizon < 0 and vertical < 0:
                # 왼쪽 위
                sol(-1, -1, 0, ans + [1] * abs(horizon) + [3] * abs(vertical))
            return

        for d in range(4):
            ny = y + dr[d]
            nx = x + dc[d]

            if 0 < ny <= n and 0 < nx <= m:
                sol(ny, nx, remain-1, ans + [d])
                break

    sol(x, y, k, [])

    return answer
