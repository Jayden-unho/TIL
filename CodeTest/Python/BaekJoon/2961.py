import sys


N = int(sys.stdin.readline())
s_set, b_set = 1, 1
s_li = [1]

for _ in range(N):
    S, B = map(int, sys.stdin.readline().split())

    b_set |= (b_set << B)

    for a in s_li:
        s_set |= (1 << (a * S))
    s_li.append(S)

    print(bin(s_set >> 1))
    print(bin(b_set >> 1))