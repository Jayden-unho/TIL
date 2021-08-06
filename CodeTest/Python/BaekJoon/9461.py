import sys

test_case = int(sys.stdin.readline())
answer = [0, 1, 1, 1, 2, 2] # 0은 무시, 1번째부터 5번째까지 정답들

for idx in range(6, 101):
    answer.append(answer[idx-3] + answer[idx-2])

for _ in range(test_case):
    num = int(sys.stdin.readline())

    print(answer[num])