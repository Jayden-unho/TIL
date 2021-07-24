testCase = int(input())

for i in range(1, testCase+1):
    num_list = list(map(int, input().split()))
    avg = 0

    for n in num_list:
        avg += n
    avg = int(round(avg/len(num_list), 0))

    print(f'#{i} {avg}')