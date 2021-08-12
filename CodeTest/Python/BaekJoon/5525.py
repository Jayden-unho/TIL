import sys


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
in_str = sys.stdin.readline().strip() + '.'

stack = []
answer = 0

for c in in_str:
    if stack == []:
        if c == 'I':
            stack.append(c)
    else:
        if c == 'O' and stack[-1] == 'I':
            stack.append(c)
        elif c == 'I' and stack[-1] == 'O':
            stack.append(c)
        else:
            tmp = (len(stack)-(2*n+1))//2 + 1
            if tmp > 0:
                answer += tmp
            stack.clear()
            if c == 'I':
                stack.append(c)



print(answer)