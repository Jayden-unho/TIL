import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
cranes = sorted(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
boxes = sorted(list(map(int, sys.stdin.readline().split())))
answer = -1

cnts = [0] * N

# 무게 제한이 작은 크레인부터 순회
# 각 크레인으로만 이동 가능한 박스 개수
c, b = 0, 0
while b < M and c < N:
    if boxes[b] <= cranes[c]:
        cnts[c] += 1
        b += 1
    else:
        c += 1

if c != N:
    # 무게제한이 가장 큰 크레인의 이동 시간
    max_ans = cnts[-1]

    # 무게제한이 큰 두번째 크레인부터 순회
    for i in range(N-2, -1, -1):

        # 현재 크레인 이동 시간 > 현재까지 최대 이동 시간
        if cnts[i] > max_ans:
            remain = cnts[i] - max_ans
            cnts[i] = max_ans

            # 현재 크레인부터 무게 제한 높은 크레인으로 순회하여 최대 이동시간만큼 박스를 나누기
            for j in range(i, N):
                if not remain:
                    break
                elif cnts[j] != max_ans:
                    num = min(remain, max_ans - cnts[j])
                    remain -= num
                    cnts[j] += num

            # 나눠야할 박스가 남아있다면, 이동시간을 늘려가며 추가
            if remain:
                for j in range(N-1, i-1, -1):
                    num = remain // (j-i+1)
                    cnts[j] += num
                    remain -= num
                max_ans = max(max_ans, max(cnts[i:]))
    answer = max(cnts)

print(answer)
