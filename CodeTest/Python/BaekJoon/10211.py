import sys
sys.stdin = open('input.txt')


T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    li = [0] + list(map(int, sys.stdin.readline().split()))
    answer = li[1]

    for idx in range(1, N+1):
        li[idx] = li[idx] + li[idx-1]
        for a in range(1, idx+1):
            tmp = li[idx] - li[a-1]
            if tmp > answer:
                answer = tmp

    print(answer)