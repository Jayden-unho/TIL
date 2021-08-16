'''
문자열을 1~8 글자 단위로 잘라서 압축하여야 합
1. 딱 맞게 잘라야함 -> 문자열 길이의 약수를 먼저 구해야 함
2. 브루트포스 알고리즘 이용
3. 문자열이 압축되지 않으면 초기 문자열 길이 반환
4. 연속으로 반복되는게 1개밖에 없으면 숫자 1은 넣지 않음
'''


def solution(s):
    possible_len = []
    answer = len(s)

    for i in range(1, 9):
        if answer%i == 0:                       # 나누어 떨어지면 해당 길이만큼 패턴을 찾아볼수있음
            possible_len.append(i)

    for l in possible_len:                      # 자르기 가능한 길이들만 반복
        tmp_stack = []
        
        for idx in range(0, len(s)-l+1, l):
            tmp_stack.append(s[idx:idx+l])      # 해당 길이만큼 잘라서 스택에 저장
        
        cnt = 1
        tmp_answer = ''
        for idx in range(1, len(tmp_stack)):
            if tmp_stack[idx-1] == tmp_stack[idx]:
                cnt += 1
            elif tmp_stack[idx-1] != tmp_stack[idx]:
                if cnt == 1:
                    tmp_answer += tmp_stack[idx-1]
                else:
                    tmp_answer += str(cnt) + tmp_stack[idx-1]
                cnt = 1
            
        if cnt == 1:
            tmp_answer += tmp_stack[idx-1]
        else:
            tmp_answer += str(cnt) + tmp_stack[idx-1]

        if answer > len(tmp_answer):
            answer = len(tmp_answer)


    return answer        



# print(solution("aabbaccc"))                 # 7
# print(solution("ababcdcdababcdcd"))         # 9
print(solution("abcabcdede"))               # 8
print(solution("abcabcabcabcdededededede")) # 14
print(solution("xababcdcdababcdcd"))        # 17