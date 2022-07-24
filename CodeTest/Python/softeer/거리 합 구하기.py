from dis import dis
import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
distance = [[1e10] * N for _ in range(N)]

for _ in range(N-1):
    x, y, t = map(int, sys.stdin.readline().split())
    distance[x-1][y-1] = min(t, distance[x-1][y-1])
    distance[y-1][x-1] = min(t, distance[y-1][x-1])

for k in range(N):
    distance[k][k] = 0
    for i in range(N):
        for j in range(N):
            distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

for i in range(N):
    print(sum(distance[i]))