import sys
sys.stdin = open("input.txt")


def get_minutes(times):
    """
    HHMM 을 분으로 계산하여 반환
    단, 문제 조건으로 0900 이 시작점이므로 해당하는 시간만큼 차감
    """
    return int(times[:2]) * 60 + int(times[2:]) - 9 * 60


N, T, P = map(int, sys.stdin.readline().split())
table = [[False] * N for _ in range(721)]
reservations = []
answer = 0

for _ in range(T):
    start, end = sys.stdin.readline().split()
    start_minutes, end_minutes = get_minutes(start), get_minutes(end)
    reservations.append((start_minutes, end_minutes))

for start, end in sorted(reservations, key=lambda x: (x[0], x[1])):
    max_dist = 0
    seat = 0

    used = []
    for i in range(N):
        if table[start][i] == True:
            used.append(i)

    for i in range(N):
        if table[start][i]:
            continue

        dist = 1e10
        for u in used:
            gap = abs(u-i)
            dist = min(dist, gap)

        if max_dist < dist:
            max_dist = dist
            seat = i

    for t in range(start, end):
        table[t][seat] = True

for t in range(720):
    if not table[t][P-1]:
        answer += 1

print(answer)
