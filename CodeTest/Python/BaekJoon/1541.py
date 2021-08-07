import sys



in_str = sys.stdin.readline()
sign = 1    # sign 이 1이면 더하기, -1이면 빼기
plus = '0'
minus = '0'

plus_stack = []
minus_stack = []

for c in in_str:
    if not c.isdigit():
        if sign == -1:
            minus_stack.append(int(minus))
            minus = '0'
        elif c == '-':
            sign *= -1
        plus_stack.append(int(plus))
        plus = '0'
    else:
        if sign == 1:
            plus += c
        else:
            minus += c

print(sum(plus_stack)-sum(minus_stack))