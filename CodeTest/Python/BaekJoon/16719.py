import sys
sys.stdin = open('input.txt')


def sol(l, r):
    if l >= r:
        return

    sorted_li = sorted(li[l:r], reverse=True, key=lambda x: (x[1], x[0]))
    idx, char = sorted_li.pop()

    answer[idx] = char
    print(''.join(answer))

    sol(idx+1, r)
    sol(l, idx)


S = sys.stdin.readline().strip()
answer = [''] * len(S)
li = list(enumerate(S))

sol(0, len(S))
