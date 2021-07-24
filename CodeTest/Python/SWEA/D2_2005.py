# 재귀함수(?)
def pascal_triangle(n):
    # base case
    if n == 1:
        now_list = ['1']
        print(' '.join(now_list))
        return now_list
    else:
        pre_list = pascal_triangle(n-1)

        now_list = []
        now_list.append('1')        
        for j in range(len(pre_list)-1):
            now_list.append(str(int(pre_list[j]) + int(pre_list[j+1])))
        now_list.append('1')

        print(' '.join(now_list))
        return now_list


testCase = int(input())

for i in range(1, testCase+1):
    number = int(input())
    print(f'#{i}')
    pascal_triangle(number)


# 반복문 사용
'''
testCase = int(input())

for i in range(1, testCase+1):
    number = int(input())
    print(f'#{i}')

    now_answer = []
    pre_answer = [1]
    
    for k in range(number):
        pre_answer = list(map(str, pre_answer))
        print(' '.join(pre_answer))
        
        if k == number-1:
            break

        now_answer.append(1)
        
        # 이전꺼로 값
        for j in range(len(pre_answer)-1):
            now_answer.append(int(pre_answer[j]) + int(pre_answer[j+1]))

        now_answer.append(1)

        pre_answer = now_answer
        now_answer = []
'''