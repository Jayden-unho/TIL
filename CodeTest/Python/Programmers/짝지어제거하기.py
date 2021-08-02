def solution(s):
    stack = []

    for c in s:
        if stack == []:
            stack.append(c)
            continue
        
        if stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    
    if stack:
        return 0
    else:
        return 1


print(solution('baabaa'))
print(solution('cdcd'))