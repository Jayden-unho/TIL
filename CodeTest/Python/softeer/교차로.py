import sys
from collections import deque
from bisect import bisect_left
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())

time_table = {}
waiting = [deque() for _ in range(4)]
answers = [-1] * N

for i in range(N):
    t, d = sys.stdin.readline().split()
    d = ord(d) - 65
    time_table[int(t)] = time_table.get(int(t), []) + [(i, d)]


t = 0
times = sorted(time_table.keys())
T = len(times)

now_waiting = 0
while True:
    lock = 4
    can_direction = []

    if time_table.get(t, False):
        for i, d in time_table[t]:
            waiting[d].append(i)
            now_waiting += 1
    
    if not now_waiting:
        next_t_idx = bisect_left(times, t)
        if next_t_idx < T:
            t = times[next_t_idx]
            continue

    for k in range(4):
        right = (k-1) % 4
        if waiting[k] and not waiting[right]:
            can_direction.append(k)
    
    for k in can_direction:
        out = waiting[k].popleft()
        answers[out] = t
        lock -= 1
        now_waiting -= 1

    if lock == 4:
        break

    t += 1

for i in range(N):
    print(answers[i])