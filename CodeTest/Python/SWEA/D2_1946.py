testCase = int(input())

for i in range(1, testCase+1):
    number = int(input())
    answer = []

    while number > 0:
        c, num = input().split()
        num = int(num)

        while num > 0:
            answer.append(c)
            num -= 1
        number -= 1
    
    print(f'#{i}')
    while answer:
        for j in range(10):
            if not answer:
                break
            print(answer.pop(0), end='')
        print()