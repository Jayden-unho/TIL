from collections import deque


def get_cipher(num):
    if not num:
        return -1

    idx = 0
    while not num % 10:
        idx += 1
        num //= 10

    return idx


def solution(storey):
    dp = {}
    dp[storey] = 0

    idx = get_cipher(storey)

    q = deque([[storey, idx]])
    while q and not dp.get(0, False):
        num, idx = q.popleft()
        minus, plus = num - 10 ** idx, num + 10 ** idx

        if not dp.get(minus, False):
            dp[minus] = dp[num] + 1
            if not minus % 10 ** (idx + 1):
                idx = get_cipher(minus)
            q.append((minus, idx))

        if not dp.get(plus, False):
            dp[plus] = dp[num] + 1
            if not plus % 10 ** (idx + 1):
                idx = get_cipher(plus)
            q.append((plus, idx))

    return dp[0]


print(solution(16))
print(solution(2554))
print(solution(120))
print(solution(999))
print(solution(678))
