testCase = int(input())

for i in range(1, testCase+1):
    number = int(input())
    
    # 값이 중복되서 들어올 필요가 없으므로 집합으로 선언
    answer = set()
    
    x = 0
    # 0~9까지 모두 들어오면 길이는 10이 된다
    while len(answer) != 10:
        x += 1
        tmp = number*x

        while tmp > 0:
            answer.add(tmp%10)
            tmp //= 10
    
    print(f'#{i} {number*x}')