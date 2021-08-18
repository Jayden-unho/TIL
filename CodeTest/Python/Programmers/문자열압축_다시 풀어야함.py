'''
문자열을 1~8 글자 단위로 잘라서 압축하여야 합
1. 딱 맞게 잘라야함 -> 문자열 길이의 약수를 먼저 구해야 함
2. 브루트포스 알고리즘 이용
3. 문자열이 압축되지 않으면 초기 문자열 길이 반환
4. 연속으로 반복되는게 1개밖에 없으면 숫자 1은 넣지 않음
'''


def solution(s):
    answer = len(s)             # 압축이 안되면 기존 문자열 길이가 가장 짧으므로

    idx = 1
    while idx <= 8:
        tmp_stack = []
        for i in range(0, len(s), idx):
            if i > len(s)-idx:
                tmp_stack.append(s[i:])
                break
            tmp_stack.append(s[i:i+idx])

        tmp_answer = []
        cnt = 1
        for i in range(1, len(tmp_stack)):
            if tmp_stack[i-1] == tmp_stack[i]:
                cnt += 1
            elif tmp_stack[i-1] != tmp_stack[i]:
                if cnt == 1:
                    tmp_answer.append(tmp_stack[i-1])
                else:
                    tmp_answer.append(str(cnt) + tmp_stack[i-1])
                cnt = 1
        if cnt == 1:
            tmp_answer.append(tmp_stack[i])
        else:
            tmp_answer.append(str(cnt) + tmp_stack[i])
        
        tmp_answer_len = len(''.join(tmp_answer))
        if answer > tmp_answer_len:
            answer = tmp_answer_len
        
        idx += 1

    return answer        



print(solution("aabbaccc"))                 # 7
print(solution("ababcdcdababcdcd"))         # 9
print(solution("abcabcdede"))               # 8
print(solution("abcabcabcabcdededededede")) # 14
print(solution("xababcdcdababcdcd"))        # 17
print(solution('abc'))
print(solution('bababbb'))