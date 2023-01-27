import sys
sys.stdin = open('input.txt')


def sol(n, ans):
    global answer

    if n == N:
        answer = max(answer, ans)
        return
    elif n > N:
        return

    next_day, price = schedules[n]
    sol(next_day, ans + price)
    sol(n+1, ans)


N = int(sys.stdin.readline())
schedules = [[] for _ in range(N)]
answer = 0

for i in range(N):
    T, P = map(int, sys.stdin.readline().split())
    schedules[i] = (T+i, P)

sol(0, 0)

print(answer)
