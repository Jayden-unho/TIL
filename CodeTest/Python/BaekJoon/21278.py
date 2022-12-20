import sys
from itertools import combinations
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())
distance = [[1e10] * N for _ in range(N)]

for _ in range(M):
    a, b = map(lambda x: int(x)-1, sys.stdin.readline().split())
    distance[a][b] = 2
    distance[b][a] = 2

for k in range(N):
    distance[k][k] = 0
    for i in range(N):
        for j in range(N):
            distance[i][j] = min(
                distance[i][j], distance[i][k] + distance[k][j])

min_distance = 1e10
answer = (-1, -1)
for a, b in combinations(range(N), 2):
    dist = sum(map(lambda x: min(x[0], x[1]), zip(distance[a], distance[b])))
    if dist < min_distance:
        min_distance = dist
        answer = (a+1, b+1)

print(*answer, min_distance)
