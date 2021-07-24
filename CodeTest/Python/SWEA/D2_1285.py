testCase = int(input())

for i in range(1, testCase+1):
    num = int(input())

    answer = list(map(lambda x: abs(int(x)), input().split()))
    answer = sorted(answer)

    print(f'#{i} {answer[0]} {answer.count(answer[0])}')