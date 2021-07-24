testCase = int(input())

for i in range(1, testCase+1):
    num1, num2 = map(int, input().split())
    sign = ''

    if num1 > num2:
        sign = '>'
    elif num1 < num2:
        sign = '<'
    else:
        sign = '='
    
    print(f'#{i} {sign}')