import sys
sys.stdin = open('input.txt')

infix = sys.stdin.readline().rstrip()                       # 중위 표현법

answer = []                                                 # 후위 표현법으로 변형된 정답
op = []                                                     # 괄호 및 연산자가 들어갈 스택

for c in infix:                                             # 앞에서부터 반복
    if c.isalpha():                                         # 알파벳이라면 바로 정답에 넣기
        answer.append(c)
    elif c == '(':                                          # 여는 괄호가 나타나면 연산자 스택에 쌓기
        op.append(c)
    elif c == ')':                                          # 닫는 괄호가 나오면 여는 괄호가 나오기 전까지의 연산들 모두 진행 필요
        while op and op[-1] != '(':                         
            answer.append(op.pop())
        op.pop()                                            # 여는 괄호는 제거
    elif c == '+' or c == '-':                              # +나 - 는 우선순위가 제일 낮으므로 앞에 있던 연산자들 모두 연산 처리
        while op and op[-1] != '(':
            answer.append(op.pop())
        op.append(c)                                        # 현재 나온 연산자는 연산자 스택에 추가
    elif c == '*' or c == '/':                                                  # *나 / 연산자는 우선순위가 상대적으로 높으므로
        while op and op[-1] != '(' and (op[-1] != '+' and op[-1] != '-'):       # 이전에 쌓인 연산자가 +나 - 가 아니면 연산 처리
            answer.append(op.pop())
        op.append(c)

answer.extend(op[::-1])             # 남아 있는 연산자들 모두 추가

print(''.join(answer))