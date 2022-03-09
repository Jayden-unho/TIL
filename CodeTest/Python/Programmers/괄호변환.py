def solution(p):
    # 올바른 괄호 문자열인지 판별
    def is_right(s):
        stack = []                      # 괄호를 쌓아놓 리스트
        for c in s:         
            if c == '(':                # 현재 괄호가 여는 괄호라면
                stack.append('(')       # 리스트에 저장
            elif not stack:             # 닫는 괄호인데, 이전에 여는 괄호가 없었다면
                return False            # 올바른 괄호가 아님
            elif stack[-1] == '(':      # 현재 괄호가 닫는 괄호인데, 바로 이전 괄호가 여는 괄호였으면
                stack.pop()             # 여는 괄호 삭제
        return True                     # 모든 괄호를 반복 완료시 올바른 괄호가 맞음

    # 주어진 괄호를 두개의 부분으로 나누는 함수
    def separate(s):
        if not s:                                   # 공백이라면
            return s, s                             # 공백 반환 (출력값이 두개여야 하므로, 공백 두개 반환)

        cnt = 0                                     # 균형잡힌 괄호를 반환하면 되므로, 개수가 서로 맞는지만 확인 필요
        for idx in range(len(s)):
            cnt += 1 if s[idx] == '(' else -1       # 현재 괄호가 여는 괄호면 +1, 닫는 괄호면 -1
            if not cnt:                             # 균형잡힌 괄호가 맞다면, 반복 종료
                break           
        return s[:idx+1], s[idx+1:]                 # 반복이 멈춘 인덱스를 기준으로 두개의 괄호로 나누어서 반환

    # 주어진 조건으로 진행하는 함수, 재귀 호출
    def solution(s):
        if is_right(s):                             # 비어있는 문자열이라면, 바로 반환
            return s

        u, v = separate(s)                          # 두개의 괄호로 나눔
        if is_right(u):                             # u가 올바른 괄호라면
            return u + solution(v)                  # v를 재귀 호출하여 처음 과정 반복하고, 그 결과를 u 뒤에 붙여서 반환
        else:                                       # u가 올바른 괄호가 아니라면
            reverse_bracket = []                    # u의 괄호들을 뒤집어서 저장하는 리스트
            for c in u[1:-1]:                       # u의 앞뒤를 삭제하고, 남아 있는 괄호들을 뒤집음
                if c == '(':
                    reverse_bracket.append(')')
                else:
                    reverse_bracket.append('(')

            return '(' + solution(v) + ')' + ''.join(reverse_bracket)   # 조건에 맞게 괄호들을 붙임

    return solution(p)


print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))