testCase = int(input())

for i in range(1, testCase+1):
    a, b = map(int, input().split())
    quota, remainder = divmod(a,b)
    print(f'#{i} {quota} {remainder}')