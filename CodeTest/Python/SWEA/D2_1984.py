testCase = int(input())

for i in range(1, testCase+1):
    num_list = list(map(int, input().split()))
    num_list.sort()
    avg = sum(num_list[1:-1]) / (len(num_list)-2)
    print(f'#{i} {round(avg)}')