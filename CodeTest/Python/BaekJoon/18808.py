import sys
sys.stdin = open('input.txt')


def is_patch(sticker, start_r, start_c, R, C):
    for r in range(R):
        for c in range(C):
            if labtop[start_r + r][start_c + c] and sticker[r][c]:
                return False
    return True


def patch(sticker, start_r, start_c, R, C):
    global answer

    for r in range(R):
        for c in range(C):
            if sticker[r][c]:
                answer += 1
                labtop[start_r + r][start_c + c] = True


def sol(sticker):
    for _ in range(4):
        R = len(sticker)
        C = len(sticker[0])

        for i in range(N-R+1):
            for j in range(M-C+1):
                if is_patch(sticker, i, j, R, C):
                    patch(sticker, i, j, R, C)
                    return

        sticker = list(zip(*sticker[::-1]))


N, M, K = map(int, sys.stdin.readline().split())
labtop = [[False] * M for _ in range(N)]
answer = 0

for _ in range(K):
    R, C = map(int, sys.stdin.readline().split())
    sticker = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]

    sol(sticker)

print(answer)
