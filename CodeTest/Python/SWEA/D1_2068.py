testCase = int(input())

for i in range(1, testCase+1):
    num_list = list(map(int, input().split()))
    
    print(f'#{i} {max(num_list)}')
