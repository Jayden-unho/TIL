# 학생의 번호와 성적등을 딕셔너리 형태로 담으려 시도함
# dictionary 는 시퀀스형이 아니라서 성적순서대로 인덱스를 이용해 접근이 불가능
# 따라서, 순서대로 학점을 주기 어려움
'''
testCase = int(input())

for i in range(1, testCase+1):
    number, student = map(int, input().split())
    grade = {}

    for j in range(1, number+1):
        test1, test2, homework = map(int, input().split())
        total_score = (test1*0.35) + (test2*0.45) + (homework*0.2)

        grade[j] = total_score

    # value 값을 기준으로 내림차순
    # key 값을 기준으로 정렬할 경우에는 .keys() or .items() 사용가능
    # value는 .items() 이용하여 키와 값을 튜플 형식으로 가져온다. (키, 값)
    # 람다를 사용해서 sorted의 key 옵션에 값을 넣는다. (item[1] - value)
    grade = sorted(grade.items(), key=lambda item:item[1], reverse=True)


    # 학점 넣어주기
'''
import sys
from pprint import pprint

sys.stdin = open('input.txt','r')

# 2차원 배열을 이용하여, 1차원에서는 학생들 하나하나를 나타냄
# 2차원의 리스트에서는 한 학생의 [번호, 총점, 학점] 을 담아서 표현
testCase = int(input())

for i in range(1, testCase+1):
    cnt_student, want_student = map(int, input().split())
    grade = []

    # 학생들 하나하나 값을 받아옴
    for j in range(1, cnt_student+1):
        test1, test2, hw = map(int, input().split())
        total_score = test1*0.35 + test2*0.45 + hw*0.2
        
        # 리스트를 집어넣음
        grade.append(list((j, total_score)))


    # 총점순으로 내림차순
    grade = sorted(grade, key=lambda student: student[1], reverse=True)

    # 학점 나누기 및 입력하기
    assignment = cnt_student//10
    for k in range(cnt_student):
        sign = k//assignment
        if sign == 0: grade[k].append('A+')
        elif sign == 1: grade[k].append('A0')
        elif sign == 2: grade[k].append('A-')
        elif sign == 3: grade[k].append('B+')
        elif sign == 4: grade[k].append('B0')
        elif sign == 5: grade[k].append('B-')
        elif sign == 6: grade[k].append('C+')
        elif sign == 7: grade[k].append('C0')
        elif sign == 8: grade[k].append('C-')
        elif sign == 9: grade[k].append('D0')

        if grade[k][0] == want_student:
            answer = grade[k][2]
            break
    
    print(f'#{i} {answer}')