import sys
sys.stdin = open('input.txt')


N, K = map(int, sys.stdin.readline().split())
durable = list(map(int, sys.stdin.readline().split()))

length = 2 * N
belt = {}
cnt_zero, answer = 0, 0
in_robot, out_robot = 0, N - 1

while cnt_zero < K:
    answer += 1

    # 1
    in_robot = (in_robot - 1) % length
    out_robot = (out_robot - 1) % length
    if belt.get(out_robot, False):
        belt[out_robot] = False

    # 2
    out = out_robot
    while out != in_robot:
        next = out
        out = (out - 1) % length

        if belt.get(out, False) and not belt.get(next, False) and durable[next]:
            belt[out] = False
            durable[next] -= 1
            if not durable[next]:
                cnt_zero += 1
            if next != out_robot:
                belt[next] = True

    # 3
    if durable[in_robot]:
        belt[in_robot] = True
        durable[in_robot] -= 1
        if not durable[in_robot]:
            cnt_zero += 1

print(answer)
