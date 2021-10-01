import sys
sys.stdin = open('input.txt')


N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

answer = [0] * N
answer[0] = 1

for i in range(N):
    if not answer[i]:
        answer[i] = answer[i] | (1 << 1)
    for j in range(i+1, N):
        answer[j] |= (answer[i] & arr[i][j])
    
print(*answer)