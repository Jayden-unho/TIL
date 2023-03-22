import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
buildings = list(map(int, sys.stdin.readline().split()))
answer = 0

for i in range(N):
    ans = 0
    height = buildings[i]

    left_slope = 1e10
    for left in range(i-1, -1, -1):
        slope = (height-buildings[left]) / (i-left)
        if slope < left_slope:
            left_slope = slope
            ans += 1

    right_slope = -1e10
    for right in range(i+1, N):
        slope = (height-buildings[right]) / (i-right)
        if slope > right_slope:
            right_slope = slope
            ans += 1

    answer = max(answer, ans)

print(answer)
