testCase = int(input())

for index in range(1, testCase+1):
    num1, num2 = map(int, input().split())
    answer = []

    num1_list = list(map(int, input().split()))
    num2_list = list(map(int, input().split()))

    # num1이 항상 더 길게 하기 위해서 num2가 더 긴 경우에 서로 값을 바꿈
    if num2 > num1:
        num1, num2 = num2, num1
        num1_list, num2_list = num2_list, num1_list

    # for
    for i in range(num1-num2+1):
        # num1에서 num2의 사이즈만큼 위치별로 값을 잘라서 가져올 임시 변수
        num1_tmp = []
        for j in range(i, i+num2):
            num1_tmp.append(num1_list[j])
        
        tmp = 0
        for k in range(num2):
            tmp += num1_tmp[k] * num2_list[k]
        answer.append(tmp)
    
    print(f'#{index} {max(answer)}')