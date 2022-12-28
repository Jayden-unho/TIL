import sys
from collections import deque
sys.stdin = open('input.txt')


def calculate(q):
    result = []

    while q:
        c = q.popleft()

        if str(c).isdigit():
            if result:
                operate = result.pop()
                left = result.pop()
                value = eval(''.join([left, operate, c]))
                result.append(str(value))
            else:
                result.append(str(c))
        elif c in {'+', '-', '*'}:
            result.append(c)
        elif c == '(':
            left = q.popleft()
            operate = q.popleft()
            if operate != ')':
                right = q.popleft()
                value = eval(''.join([left, operate, right]))
            else:
                value = left

            if result:
                operate = result.pop()
                left = result.pop()
                value = eval(''.join([left, operate, str(value)]))
            result.append(str(value))
        elif c == ')':
            pass

    return int(result[0])


def sol(n, ans, open):
    global answer

    if n == N:
        if open:
            ans.append(')')
        answer = max(answer, calculate(deque(ans)))
        return

    c = formula[n]
    if c.isdigit():
        if open:
            sol(n+1, ans + [c, ')'], False)
        else:
            sol(n+1, ans + ['(', c], True)
            sol(n+1, ans + [c], False)
    else:
        sol(n+1, ans + [c], open)


N = int(sys.stdin.readline())
formula = list(sys.stdin.readline().rstrip())

selected = [False] * N
answer = -1e10

sol(0, [], False)
print(answer)
