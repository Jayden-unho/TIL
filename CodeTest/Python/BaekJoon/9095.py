import sys



test_case = int(sys.stdin.readline())

# 1, 2, 3 의 값을 넣어줌
answer = [1, 2, 4]
for idx in range(3, 11):
    answer.append(answer[idx-3] + answer[idx-2] + answer[idx-1])

for _ in range(test_case):
    num = int(sys.stdin.readline())

    print(answer[num-1])