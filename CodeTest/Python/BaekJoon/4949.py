import sys

while True:
    in_str = sys.stdin.readline().rstrip()
    answer_list = []

    if in_str == '.':
        break
    
    for c in in_str:
        if c == '(' or c == ')' or c == '[' or c == ']':
            if len(answer_list) == 0:
                answer_list.append(c)
            else:
                tmp = answer_list.pop()
                if c == ')' and tmp == '(': pass
                elif c == ']' and tmp == '[': pass
                else:
                    answer_list.append(tmp)
                    answer_list.append(c)

    if len(answer_list) == 0: print('yes')
    else: print('no')
    