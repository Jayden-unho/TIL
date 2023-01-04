import sys
sys.stdin = open('input.txt')

N, C = map(int, sys.stdin.readline().split())
M = int(sys.stdin.readline())
infos = sorted([list(map(int, sys.stdin.readline().split()))
               for _ in range(M)], key=lambda x: (x[1], x[0]))

truck = [C] * N
answer = 0

for S, E, amount in infos:
    num = min(C, amount, *truck[S-1:E])

    for i in range(S, E):
        truck[i-1] -= num
    answer += num

print(answer)
