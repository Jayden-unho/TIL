testCase = int(input())

for i in range(1, testCase+1):
    number = int(input())
    answer = 0

    n = 1
    while n <= number:
        if n%2: answer += n
        else: answer -= n
        n += 1
    
    print(f'#{i} {answer}')