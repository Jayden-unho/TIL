import sys


num = int(sys.stdin.readline())
stack = []
answer = []
idx = 1

for _ in range(num):
    in_num = int(sys.stdin.readline())


    while idx <= in_num:
        stack.append(idx)
        answer.append('+')
        idx += 1
    
    if in_num == stack[-1]:
        stack.pop()
        answer.append('-')

if stack == []:
    for v in answer:
        print(v)
else:
    print('NO')