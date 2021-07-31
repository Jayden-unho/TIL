import sys

testCase = int(sys.stdin.readline())

for _ in range(testCase):
    in_str = sys.stdin.readline().rstrip()
    answer = 'YES'
    stack = []

    for c in in_str:
        if c == '(':
            stack.append(c)
        else:
            if stack == []:
                answer = 'NO'
                break
            else:
                tmp = stack.pop()
                if tmp == ')' and c != '(':
                    answer = 'NO'
                    break
    if stack != []:
        answer = 'NO'

    print(answer)    