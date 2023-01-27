import sys
from copy import deepcopy
sys.stdin = open('input.txt')


def up(arr):
    for c in range(N):
        idx = 0
        for r in range(1, N):
            num = arr[r][c]
            arr[r][c] = 0
            if not num:
                continue

            if not arr[idx][c]:
                arr[idx][c] = num
            elif arr[idx][c] == num:
                arr[idx][c] += num
                idx += 1
            elif arr[idx][c] != num:
                idx += 1
                arr[idx][c] = num
    return arr


def down(arr):
    for c in range(N):
        idx = N - 1
        for r in range(N-2, -1, -1):
            num = arr[r][c]
            arr[r][c] = 0

            if not num:
                continue

            if not arr[idx][c]:
                arr[idx][c] = num
            elif arr[idx][c] == num:
                arr[idx][c] *= 2
                idx -= 1
            elif arr[idx][c] != num:
                idx -= 1
                arr[idx][c] = num
    return arr


def left(arr):
    for r in range(N):
        idx = 0
        for c in range(1, N):
            num = arr[r][c]
            arr[r][c] = 0

            if not num:
                continue

            if not arr[r][idx]:
                arr[r][idx] = num
            elif arr[r][idx] == num:
                arr[r][idx] += num
                idx += 1
            elif arr[r][idx] != num:
                idx += 1
                arr[r][idx] = num
    return arr


def right(arr):
    for r in range(N):
        idx = N - 1
        for c in range(N-2, -1, -1):
            num = arr[r][c]
            arr[r][c] = 0

            if not num:
                continue

            if not arr[r][idx]:
                arr[r][idx] = num
            elif arr[r][idx] == num:
                arr[r][idx] *= 2
                idx -= 1
            elif arr[r][idx] != num:
                idx -= 1
                arr[r][idx] = num
    return arr


def sol(n, arr):
    global answer

    if n == 5:
        for i in range(N):
            answer = max(answer, *arr[i])
        return

    sol(n+1, up(deepcopy(arr)))
    sol(n+1, down(deepcopy(arr)))
    sol(n+1, left(deepcopy(arr)))
    sol(n+1, right(deepcopy(arr)))


N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer = 0


sol(0, board)
print(answer)
