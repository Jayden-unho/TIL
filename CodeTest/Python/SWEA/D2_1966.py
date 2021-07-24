testCase = int(input())

for i in range(1, testCase+1):
    num = int(input())
    num_list = list(map(int, input().split()))

    num_list = list(map(str, sorted(num_list)))

    print(f'#{i}', end=' ')
    print(' '.join(num_list))