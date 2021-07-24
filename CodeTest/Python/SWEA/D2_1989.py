testCase = int(input())

for i in range(1, testCase+1):
    in_str = input()
    reverse_str = ''
    answer = 0

    for c in in_str:
        reverse_str = c + reverse_str
    
    if reverse_str == in_str:
        answer = 1

    print(f'#{i} {answer}')