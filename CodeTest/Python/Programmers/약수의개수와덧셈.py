def solution(left, right):
    answer = 0

    for n in range(left, right+1):
        if int(n**0.5) ** 2 == n:
            answer -= n
        else:
            answer += n

    return answer


print(solution(13, 17))
print(solution(24, 27))