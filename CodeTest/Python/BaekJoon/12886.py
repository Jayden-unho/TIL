import sys
from collections import deque
sys.stdin = open('input.txt')


def set_new_group(left, right, etc):
    if left < right:
        key = [left * 2, right - left, etc]
    else:
        key = [left - right, right * 2, etc]

    return tuple(sorted(key))


def sol():
    init_key = tuple(sorted([A, B, C]))
    q = deque([init_key])

    while q:
        key = q.popleft()
        a, b, c = key
        if visited.get(key, False):
            continue
        elif a == b and b == c:
            return 1

        visited[key] = True
        if a != b:
            key = set_new_group(a, b, c)
            q.append(key)
        if a != c:
            key = set_new_group(a, c, b)
            q.append(key)
        if b != c:
            key = set_new_group(b, c, a)
            q.append(key)

    return 0


A, B, C = map(int, sys.stdin.readline().split())
visited = {}

print(sol())
