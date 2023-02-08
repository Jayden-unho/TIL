import sys
sys.stdin = open('input.txt')


def binary_search():
    l, r = 0, 1e11
    result = -1

    while l <= r:
        mid = (l + r) // 2
        cnt = M

        for t in times:
            cnt += mid // t

        if cnt >= N:
            result = mid
            r = mid - 1
        else:
            l = mid + 1

    return result


N, M = map(int, sys.stdin.readline().split())
times = list(map(int, sys.stdin.readline().split()))

target_time = binary_search()

if target_time < 0:
    print(N)
else:
    cnt = 0
    for t in times:
        cnt += (target_time-1) // t + 1

    for i in range(M):
        if not target_time % times[i]:
            cnt += 1
        if cnt == N:
            print(i+1)
            break
