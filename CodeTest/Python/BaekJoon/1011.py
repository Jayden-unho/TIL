import sys
sys.stdin = open('input.txt')

T = int(sys.stdin.readline())

for _ in range(T):
    # 입력
    x, y = map(int, sys.stdin.readline().split())

    # 이동해야 할 거리
    distance = y - x
    # 작동 횟수, 작동 횟수당 이동 가능 거리 개수, 마지막 이동 거리
    ans, g, last_dist = 0, 0, 0

    while True:
        # 작동 횟수 증가
        ans += 1

        # 작동 횟수가 홀수라면 이동 가능한 거리 개수 1 증가
        if ans % 2:
            g += 1

        # 마지막 이동 가능 거리 변경
        last_dist += g

        # 현재 작동 횟수로 이동이 가능하면 종료
        if last_dist >= distance:
            break

    print(ans)
