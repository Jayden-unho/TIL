# 팰린드롬

import sys


# 1. 반복문 이용해서 찾기
while True:   # 입력값이 0이 들어오면 반복문 종료
    input_num = str(sys.stdin.readline().rstrip())
    answer = ''

    # 입력값이 0이면 종료
    if input_num == '0': break

    # 글자를 하나씩 가져와서 앞글자에 붙임
    for c in input_num: answer = c + answer
        
    if input_num == answer: print('yes')
    else: print('no')