def solution(n):
    answer = ''

    while n > 0:
        mod = n%3
        if mod == 0:
            mod = 4
            n -= 1
        answer = str(mod) + answer
        n //= 3

    return answer

print(solution(15))
print(solution(16))
print(solution(17))
print(solution(18))