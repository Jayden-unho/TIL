def solution(n):
    three = ''
    answer = 0

    while n:
        three += str(n%3)
        n //= 3

    i = 0
    while three:
        answer += int(three[-1]) * 3**i
        i += 1
        three = three[:-1]

    return answer

print(solution(45))
print(solution(125))