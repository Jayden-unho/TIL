import sys
sys.stdin = open('input.txt')


def binarySearch(low, high, target_idx):
    global answer_value

    while low < high:
        mid = (low+high) // 2

        if liquid[mid] < -liquid[target_idx]:
            low = mid + 1
        elif liquid[mid] > -liquid[target_idx]:
            high = mid - 1
        elif liquid[mid] == -liquid[target_idx]:
            answer_value = abs(liquid[mid] + liquid[target_idx])
            ans.clear()
            ans.extend([liquid[mid], liquid[target_idx]])
            return
    
    for j in range(-1, 2):
        if 0 <= low+j < N and low+j != target_idx:
            diff = abs(liquid[low+j] + liquid[target_idx])
            if answer_value > diff:
                answer_value = diff
                ans.clear()
                ans.extend([liquid[low+j], liquid[target_idx]])


N = int(sys.stdin.readline())
liquid = list(sorted(map(int, sys.stdin.readline().split())))
answer_value = 1e30
ans = []

for idx in range(N):
    binarySearch(0, N-1, idx)

print(*sorted(ans))